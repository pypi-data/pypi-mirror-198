import re
import textwrap
import enum
import getpass
import logging
import ntpath
import shlex
import socket
import time
from pathlib import Path
from typing import Optional

from antareslauncher.remote_environnement import iconnection
from antareslauncher.remote_environnement.iremote_environment import (
    IRemoteEnvironment,
    KillJobErrorException,
    NoLaunchScriptFoundException,
    NoRemoteBaseDirException,
    SubmitJobErrorException,
    GetJobStateError,
)
from antareslauncher.remote_environnement.slurm_script_features import (
    ScriptParametersDTO,
    SlurmScriptFeatures,
)
from antareslauncher.study_dto import StudyDTO

logger = logging.getLogger(__name__)


SLURM_STATE_FAILED = "FAILED"
SLURM_STATE_TIMEOUT = "TIMEOUT"
SLURM_STATE_CANCELLED = "CANCELLED"
SLURM_STATE_COMPLETED = "COMPLETED"
SLURM_STATE_RUNNING = "RUNNING"


class JobStateCodes(enum.Enum):
    # noinspection SpellCheckingInspection
    """
    The `sacct` command returns the status of each task in a column named State or JobState.
    The possible values for this column depend on the cluster management system
    you are using, but here are some of the most common values:
    """
    # Job terminated due to launch failure, typically due to a hardware failure
    # (e.g. unable to boot the node or block and the job can not be requeued).
    BOOT_FAIL = "BOOT_FAIL"

    # Job was explicitly cancelled by the user or system administrator.
    # The job may or may not have been initiated.
    CANCELLED = "CANCELLED"

    # Job has terminated all processes on all nodes with an exit code of zero.
    COMPLETED = "COMPLETED"

    # Job terminated on deadline.
    DEADLINE = "DEADLINE"

    # Job terminated with non-zero exit code or other failure condition.
    FAILED = "FAILED"

    # Job terminated due to failure of one or more allocated nodes.
    NODE_FAIL = "NODE_FAIL"

    # Job experienced out of memory error.
    OUT_OF_MEMORY = "OUT_OF_MEMORY"

    # Job is awaiting resource allocation.
    PENDING = "PENDING"

    # Job terminated due to preemption.
    PREEMPTED = "PREEMPTED"

    # Job currently has an allocation.
    RUNNING = "RUNNING"

    # Job was requeued.
    REQUEUED = "REQUEUED"

    # Job is about to change size.
    RESIZING = "RESIZING"

    # Sibling was removed from cluster due to other cluster starting the job.
    REVOKED = "REVOKED"

    # Job has an allocation, but execution has been suspended and
    # CPUs have been released for other jobs.
    SUSPENDED = "SUSPENDED"

    # Job terminated upon reaching its time limit.
    TIMEOUT = "TIMEOUT"


class RemoteEnvironmentWithSlurm(IRemoteEnvironment):
    """Class that represents the remote environment"""

    def __init__(
        self,
        _connection: iconnection.IConnection,
        slurm_script_features: SlurmScriptFeatures,
    ):
        super(RemoteEnvironmentWithSlurm, self).__init__(_connection=_connection)
        self.slurm_script_features = slurm_script_features
        self.remote_base_path: str = ""
        self._initialise_remote_path()
        self._check_remote_script()

    def _initialise_remote_path(self):
        self._set_remote_base_path()
        if not self.connection.make_dir(self.remote_base_path):
            raise NoRemoteBaseDirException

    def _set_remote_base_path(self):
        remote_home_dir = self.connection.home_dir
        self.remote_base_path = (
            str(remote_home_dir)
            + "/REMOTE_"
            + getpass.getuser()
            + "_"
            + socket.gethostname()
        )

    def _check_remote_script(self):
        remote_antares_script = self.slurm_script_features.solver_script_path
        if not self.connection.check_file_not_empty(remote_antares_script):
            raise NoLaunchScriptFoundException

    def get_queue_info(self):
        """This function return the information from: squeue -u run-antares

        Returns:
            The error if connection.execute_command raises an error, otherwise the slurm queue info
        """
        username = self.connection.username
        command = f"squeue -u {username} --Format=name:40,state:12,starttime:22,TimeUsed:12,timelimit:12"
        output, error = self.connection.execute_command(command)
        if error:
            return error
        else:
            return f"{username}@{self.connection.host}\n" + output

    def kill_remote_job(self, job_id):
        """Kills job with ID

        Args:
            job_id: Id of the job to kill

        Raises:
            KillJobErrorException if the command raises an error
        """

        command = f"scancel {job_id}"
        _, error = self.connection.execute_command(command)
        if error:
            raise KillJobErrorException

    @staticmethod
    def convert_time_limit_from_seconds_to_minutes(time_limit_seconds):
        """Converts time in seconds to time in minutes

        Args:
            time_limit_seconds: The time limit in seconds

        Returns:
            The value of the time limit in minutes
        """
        minimum_duration_in_minutes = 1
        time_limit_minutes = int(time_limit_seconds / 60)
        if time_limit_minutes < minimum_duration_in_minutes:
            time_limit_minutes = minimum_duration_in_minutes
        return time_limit_minutes

    def compose_launch_command(self, script_params: ScriptParametersDTO):
        return self.slurm_script_features.compose_launch_command(
            self.remote_base_path,
            script_params,
        )

    def submit_job(self, my_study: StudyDTO):
        """Submits the Antares job to slurm

        Args:
            my_study: The study data transfer object

        Returns:
            The slurm job id if the study has been submitted

        Raises:
            SubmitJobErrorException if the job has not been successfully submitted
        """
        time_limit = self.convert_time_limit_from_seconds_to_minutes(
            my_study.time_limit
        )
        script_params = ScriptParametersDTO(
            study_dir_name=Path(my_study.path).name,
            input_zipfile_name=Path(my_study.zipfile_path).name,
            time_limit=time_limit,
            n_cpu=my_study.n_cpu,
            antares_version=int(my_study.antares_version),
            run_mode=my_study.run_mode,
            post_processing=my_study.post_processing,
            other_options=my_study.other_options or "",
        )
        command = self.compose_launch_command(script_params)
        output, error = self.connection.execute_command(command)
        if error:
            raise SubmitJobErrorException
        job_id = self._get_jobid_from_output_of_submit_command(output)
        return job_id

    @staticmethod
    def _get_jobid_from_output_of_submit_command(output):
        job_id = None
        # SLURM squeue command returns f'Submitted {job_id}' if successful
        stdout_list = str(output).split()
        if stdout_list and stdout_list[0] == "Submitted":
            job_id = int(stdout_list[-1])
        return job_id

    @staticmethod
    def get_advancement_flags_from_state(state):
        """Converts the slurm state of the job to 3 boolean values

        Args:
            state: The job state string as obtained from Slurm

        Returns:
            started, finished, with_error: the booleans representing the advancement of the slurm_job
        """

        if state == SLURM_STATE_RUNNING:
            started = True
            finished = False
            with_error = False
        elif state == SLURM_STATE_COMPLETED:
            started = True
            finished = True
            with_error = False
        elif (
            state.startswith(SLURM_STATE_CANCELLED)
            or state.startswith(SLURM_STATE_TIMEOUT)
            or state == SLURM_STATE_FAILED
        ):
            started = True
            with_error = True
            finished = True
        # PENDING
        else:
            started = False
            finished = False
            with_error = False

        return started, finished, with_error

    def get_job_state_flags(
        self,
        study,
        *,
        attempts=5,
        sleep_time=0.5,
    ) -> [bool, bool, bool]:
        """
        Retrieves the current state of a SLURM job with the given job ID and name.
        Args:
            study: The study to check.
            attempts: The number of attempts to make to retrieve the job state.
            sleep_time: The amount of time to wait between attempts, in seconds.
        Returns:
            started, finished, with_error: booleans representing the advancement of the SLURM job
        Raises:
            GetJobStateErrorException: If the job state cannot be retrieved after
            the specified number of attempts.
        """
        job_state = self._retrieve_slurm_control_state(study.job_id, study.name)
        if job_state is None:
            # noinspection SpellCheckingInspection
            logger.info(
                f"Job '{study.job_id}' no longer active in SLURM,"
                f" the job status is read from the SACCT database..."
            )
            job_state = self._retrieve_slurm_acct_state(
                study.job_id,
                study.name,
                attempts=attempts,
                sleep_time=sleep_time,
            )
        if job_state is None:
            # noinspection SpellCheckingInspection
            logger.warning(
                f"Job '{study.job_id}' not found in SACCT database."
                f"Assuming it was recently launched and will start processing soon."
            )
            job_state = JobStateCodes.RUNNING
        return {
            # JobStateCodes ------ started, finished, with_error
            JobStateCodes.BOOT_FAIL: (False, False, False),
            JobStateCodes.CANCELLED: (True, True, True),
            JobStateCodes.COMPLETED: (True, True, False),
            JobStateCodes.DEADLINE: (True, True, True),  # similar to timeout
            JobStateCodes.FAILED: (True, True, True),
            JobStateCodes.NODE_FAIL: (True, True, True),
            JobStateCodes.OUT_OF_MEMORY: (True, True, True),
            JobStateCodes.PENDING: (False, False, False),
            JobStateCodes.PREEMPTED: (False, False, False),
            JobStateCodes.RUNNING: (True, False, False),
            JobStateCodes.REQUEUED: (False, False, False),
            JobStateCodes.RESIZING: (False, False, False),
            JobStateCodes.REVOKED: (False, False, False),
            JobStateCodes.SUSPENDED: (True, False, False),
            JobStateCodes.TIMEOUT: (True, True, True),
        }[job_state]

    def _retrieve_slurm_control_state(
        self,
        job_id: int,
        job_name: str,
    ) -> Optional[JobStateCodes]:
        """
        Use the `scontrol` command to retrieve job status information in SLURM.
        See: https://slurm.schedmd.com/scontrol.html
        """
        # Construct the command line arguments used to check alive jobs state.
        # noinspection SpellCheckingInspection
        args = ["scontrol", "show", "job", f"{job_id}"]
        command = " ".join(shlex.quote(arg) for arg in args)
        output, error = self.connection.execute_command(command)
        if error:
            # The command output may include an error message if the job is
            # no longer active or has been removed
            if re.search("Invalid job id specified", error):
                return None
            reason = f"The command [{command}] failed: {error}"
            raise GetJobStateError(job_id, job_name, reason)

        # We can retrieve the job state from the output of the command
        # by extracting the value of the `JobState` field.
        if match := re.search(r"JobState=(\w+)", output):
            return JobStateCodes(match[1])

        reason = (
            f"The command [{command}] return an non-parsable output:"
            f"\n{textwrap.indent(output, 'OUTPUT> ')}"
        )
        raise GetJobStateError(job_id, job_name, reason)

    def _retrieve_slurm_acct_state(
        self,
        job_id: int,
        job_name: str,
        *,
        attempts: int = 5,
        sleep_time: float = 0.5,
    ) -> Optional[JobStateCodes]:
        # Construct the command line arguments used to check the jobs state.
        # See the man page: https://slurm.schedmd.com/sacct.html
        # noinspection SpellCheckingInspection
        delimiter = ","
        # noinspection SpellCheckingInspection
        args = [
            "sacct",
            f"--jobs={job_id}",
            f"--name={job_name}",
            "--format=JobID,JobName,State",
            "--parsable2",
            f"--delimiter={delimiter}",
            "--noheader",
        ]
        command = " ".join(shlex.quote(arg) for arg in args)

        # Makes several attempts to get the job state.
        # I don't really know why, but it's better to reproduce the old behavior.
        output: Optional[str]
        last_error: str = ""
        for attempt in range(attempts):
            output, error = self.connection.execute_command(command)
            if output is not None:
                break
            last_error = error
            time.sleep(sleep_time)
        else:
            reason = (
                f"The command [{command}] failed after {attempts} attempts:"
                f" {last_error}"
            )
            raise GetJobStateError(job_id, job_name, reason)

        # When the output is empty it mean that the job is not found
        if not output.strip():
            return None

        # Parse the output to extract the job state.
        # The output must be a CSV-like string without header row.
        for line in output.splitlines():
            parts = line.split(delimiter)
            if len(parts) == 3:
                out_job_id, out_job_name, out_state = parts
                if out_job_id == str(job_id) and out_job_name == job_name:
                    # Match the first word only, e.g.: "CANCEL by 123456798"
                    job_state_str = re.match(r"(\w+)", out_state)[1]
                    return JobStateCodes(job_state_str)

        reason = (
            f"The command [{command}] return an non-parsable output:"
            f"\n{textwrap.indent(output, 'OUTPUT> ')}"
        )
        raise GetJobStateError(job_id, job_name, reason)

    def upload_file(self, src):
        """Uploads a file to the remote server

        Args:
            src: Path of the file to upload

        Returns:
            True if the file has been successfully sent, False otherwise
        """
        dst = f"{self.remote_base_path}/{Path(src).name}"
        return self.connection.upload_file(src, dst)

    def _list_remote_logs(self, job_id: int):
        """Lists the logs related to the job

        Returns:
            List containing the files name, empty if none is present
        """

        logs_path_signature = self.slurm_script_features.get_logs_path_signature(
            self.remote_base_path, job_id
        )
        command = f"ls  " + logs_path_signature
        output, error = self.connection.execute_command(command)

        def path_leaf(path):
            head, tail = ntpath.split(path)
            return tail or ntpath.basename(head)

        list_of_files = []
        if output and not error:
            list_of_files = [path_leaf(Path(file)) for file in output.splitlines()]

        return list_of_files

    def download_logs(self, study: StudyDTO):
        """Download the slurm logs of a given study

        Args:
            study: The study data transfer object

        Returns:
            True if all the logs have been downloaded, False if all the logs have not been downloaded or if there are
            no files to download
        """
        file_list = self._list_remote_logs(study.job_id)
        if file_list:
            return_flag = True
            for file in file_list:
                src = self.remote_base_path + "/" + file
                dst = str(Path(study.job_log_dir) / file)
                return_flag = return_flag and self.connection.download_file(src, dst)
        else:
            return_flag = False
        return return_flag

    def check_final_zip_not_empty(self, study: StudyDTO, final_zip_name: str):
        """Checks if finished-job.zip is not empty

        Args:
            study:
            final_zip_name:

        Returns:
            True if the final zip exists, False otherwise
        """
        return_flag = False
        if study.finished:
            filename = self.remote_base_path + "/" + final_zip_name
            if self.connection.check_file_not_empty(filename) is True:
                return_flag = True
        return return_flag

    def download_final_zip(self, study: StudyDTO):
        """Downloads the final zip containing the output fo Antares

        Args:
            study: The study that will be downloaded

        Returns:
            True if the zip has been successfully downloaded, false otherwise
        """
        final_zip_name = self.slurm_script_features.get_final_zip_name(
            study.name, study.job_id, study.run_mode
        )

        if self.check_final_zip_not_empty(study, final_zip_name):
            if study.local_final_zipfile_path:
                local_final_zipfile_path = study.local_final_zipfile_path
            else:
                local_final_zipfile_path = str(Path(study.output_dir) / final_zip_name)
                src = self.remote_base_path + "/" + final_zip_name
                dst = str(local_final_zipfile_path)
                if not self.connection.download_file(src, dst):
                    local_final_zipfile_path = None
        else:
            local_final_zipfile_path = None
        return local_final_zipfile_path

    def remove_input_zipfile(self, study: StudyDTO):
        """Removes initial zipfile

        Args:
            study: The study that will be downloaded

        Returns:
            True if the file has been successfully removed, False otherwise
        """
        if not study.input_zipfile_removed:
            zip_name = Path(study.zipfile_path).name
            study.input_zipfile_removed = self.connection.remove_file(
                f"{self.remote_base_path}/{zip_name}"
            )
        return study.input_zipfile_removed

    def remove_remote_final_zipfile(self, study: StudyDTO):
        """Removes final zipfile

        Args:
            study: The study that will be downloaded

        Returns:
            True if the file has been successfully removed, False otherwise
        """
        return self.connection.remove_file(
            f"{self.remote_base_path}/{Path(study.local_final_zipfile_path).name}"
        )

    def clean_remote_server(self, study: StudyDTO):
        """
        Removes the input and the output zipfile from the remote host

        Args:
            study: The study that will be downloaded

        Returns:
            True if all files have been removed, False otherwise
        """
        return_flag = False
        if not study.remote_server_is_clean:
            return_flag = self.remove_remote_final_zipfile(
                study
            ) & self.remove_input_zipfile(study)
        return return_flag
