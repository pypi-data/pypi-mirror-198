import getpass
import re
import shlex
import socket
from pathlib import Path
from unittest import mock
from unittest.mock import call

import pytest
from antareslauncher.remote_environnement.iremote_environment import (
    GetJobStateError,
    KillJobErrorException,
    NoLaunchScriptFoundException,
    NoRemoteBaseDirException,
    SubmitJobErrorException,
)
from antareslauncher.remote_environnement.remote_environment_with_slurm import (
    RemoteEnvironmentWithSlurm,
)
from antareslauncher.remote_environnement.slurm_script_features import (
    ScriptParametersDTO,
    SlurmScriptFeatures,
)
from antareslauncher.study_dto import Modes, StudyDTO


class TestRemoteEnvironmentWithSlurm:
    """
    Review all the tests for the Class RemoteEnvironmentWithSlurm

    Test the get_all_job_state_flags() method:

    2 given a study the output obtained from the SLURM command should be correctly interpreted (different tests should be
     created, one for each treated state): the return values of the methods should be correct

    3 given a study an exception should be raised (to be created in iremote_environment.py) if the execute_command fails

    4 given a study where study.submitted is not True we should define a return value (for example (false, false, false))

    5 given a study, if execute_command return an error then an exception should be raised

    6 if execute command return an output of length <=0 the same exception should be raised
    """

    @pytest.fixture(scope="function")
    def study(self):
        return StudyDTO(
            time_limit=60,
            path="study path",
            n_cpu=42,
            zipfile_path="zipfile_path",
            antares_version="700",
            local_final_zipfile_path="local_final_zipfile_path",
            run_mode=Modes.antares,
        )

    @pytest.fixture(scope="function")
    def remote_env(self):
        remote_home_dir = "remote_home_dir"
        connection = mock.Mock()
        connection.home_dir = remote_home_dir
        slurm_script_features = SlurmScriptFeatures("slurm_script_path")
        return RemoteEnvironmentWithSlurm(connection, slurm_script_features)

    @pytest.mark.unit_test
    def test_initialise_remote_path_calls_connection_make_dir_with_correct_arguments(
        self,
    ):
        # given
        remote_home_dir = "remote_home_dir"
        remote_base_dir = (
            f"{remote_home_dir}/REMOTE_{getpass.getuser()}_{socket.gethostname()}"
        )
        connection = mock.Mock()
        connection.home_dir = remote_home_dir
        connection.make_dir = mock.Mock(return_value=True)
        connection.check_file_not_empty = mock.Mock(return_value=True)
        slurm_script_features = SlurmScriptFeatures("slurm_script_path")
        # when
        RemoteEnvironmentWithSlurm(connection, slurm_script_features)
        # then
        connection.make_dir.assert_called_with(remote_base_dir)

    @pytest.mark.unit_test
    def test_when_constructor_is_called_and_remote_base_path_cannot_be_created_then_exception_is_raised(
        self,
    ):
        # given
        connection = mock.Mock()
        slurm_script_features = SlurmScriptFeatures("slurm_script_path")
        # when
        connection.make_dir = mock.Mock(return_value=False)
        # then
        with pytest.raises(NoRemoteBaseDirException):
            RemoteEnvironmentWithSlurm(connection, slurm_script_features)

    @pytest.mark.unit_test
    def test_when_constructor_is_called_then_connection_check_file_not_empty_is_called_with_correct_arguments(
        self,
    ):
        # given
        connection = mock.Mock()
        connection.make_dir = mock.Mock(return_value=True)
        connection.check_file_not_empty = mock.Mock(return_value=True)
        slurm_script_features = SlurmScriptFeatures("slurm_script_path")
        # when
        RemoteEnvironmentWithSlurm(connection, slurm_script_features)
        # then
        remote_script_antares = "slurm_script_path"
        connection.check_file_not_empty.assert_called_with(remote_script_antares)

    @pytest.mark.unit_test
    def test_when_constructor_is_called_and_connection_check_file_not_empty_is_false_then_exception_is_raised(
        self,
    ):
        # given
        remote_home_dir = "/applis/antares/"
        connection = mock.Mock()
        connection.home_dir = remote_home_dir
        connection.make_dir = mock.Mock(return_value=True)
        slurm_script_features = SlurmScriptFeatures("slurm_script_path")
        # when
        connection.check_file_not_empty = mock.Mock(return_value=False)
        # then
        with pytest.raises(NoLaunchScriptFoundException):
            RemoteEnvironmentWithSlurm(connection, slurm_script_features)

    @pytest.mark.unit_test
    def test_get_queue_info_calls_connection_execute_command_with_correct_argument(
        self, remote_env
    ):
        # given
        username = "username"
        host = "host"
        remote_env.connection.username = username
        remote_env.connection.host = host
        command = f"squeue -u {username} --Format=name:40,state:12,starttime:22,TimeUsed:12,timelimit:12"
        output = "output"
        error = None
        # when
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        # then
        assert remote_env.get_queue_info() == f"{username}@{host}\n{output}"
        remote_env.connection.execute_command.assert_called_with(command)

    @pytest.mark.unit_test
    def test_when_connection_exec_command_has_an_error_then_get_queue_info_returns_the_error_string(
        self, remote_env
    ):
        # given
        username = "username"
        remote_env.connection.username = username
        # when
        output = None
        error = "error"
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        # then
        assert remote_env.get_queue_info() == "error"

    @pytest.mark.unit_test
    def test_kill_remote_job_execute_scancel_command(self, remote_env):
        job_id = 42
        output = None
        error = None
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        command = f"scancel {job_id}"
        remote_env.kill_remote_job(job_id)
        remote_env.connection.execute_command.assert_called_with(command)

    @pytest.mark.unit_test
    def test_when_kill_remote_job_is_called_and_exec_command_returns_error_exception_is_raised(
        self, remote_env
    ):
        # when
        output = None
        error = "error"
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        # then
        with pytest.raises(KillJobErrorException):
            remote_env.kill_remote_job(42)

    @pytest.mark.unit_test
    def test_when_submit_job_is_called_then_execute_command_is_called_with_specific_slurm_command(
        self, remote_env, study
    ):
        # when
        output = "output"
        error = None
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        remote_env.submit_job(study)
        # then
        script_params = ScriptParametersDTO(
            study_dir_name=Path(study.path).name,
            input_zipfile_name=Path(study.zipfile_path).name,
            time_limit=1,
            n_cpu=study.n_cpu,
            antares_version=int(study.antares_version or "0"),
            run_mode=study.run_mode,
            post_processing=study.post_processing,
            other_options="",
        )
        command = remote_env.slurm_script_features.compose_launch_command(
            remote_env.remote_base_path, script_params
        )
        remote_env.connection.execute_command.assert_called_with(command)

    @pytest.mark.unit_test
    def test_when_submit_job_is_called_and_receives_submitted_420_returns_job_id_420(
        self, remote_env, study
    ):
        # when
        output = "Submitted 420"
        error = None
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        # then
        assert remote_env.submit_job(study) == 420

    @pytest.mark.unit_test
    def test_when_submit_job_is_called_and_receives_error_then_exception_is_raised(
        self, remote_env, study
    ):
        # when
        output = ""
        error = "error"
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        # then
        with pytest.raises(SubmitJobErrorException):
            remote_env.submit_job(study)

    @pytest.mark.unit_test
    def test_when_submit_job_is_called_and_receives_submitted_420_returns_job_id_420(
        self, remote_env, study
    ):
        # when
        output = "Submitted 420"
        error = None
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        # then
        assert remote_env.submit_job(study) == 420

    @pytest.mark.unit_test
    def test_when_submit_job_is_called_and_receives_error_then_exception_is_raised(
        self, remote_env, study
    ):
        # when
        output = ""
        error = "error"
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        # then
        with pytest.raises(SubmitJobErrorException):
            remote_env.submit_job(study)

    # noinspection SpellCheckingInspection
    @pytest.mark.unit_test
    def test_get_job_state_flags__scontrol_failed(self, remote_env, study):
        study.job_id = 42
        output, error = "", "invalid entity:XXX for keyword:show"
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        with pytest.raises(GetJobStateError, match=re.escape(error)) as ctx:
            remote_env.get_job_state_flags(study)
        assert output in str(ctx.value)
        command = f"scontrol show job {study.job_id}"
        remote_env.connection.execute_command.assert_called_once_with(command)

    # noinspection SpellCheckingInspection
    @pytest.mark.unit_test
    def test_get_job_state_flags__scontrol_dead_job(self, remote_env, study):
        study.job_id = 42
        job_state = "RUNNING"
        args = [
            "sacct",
            f"--jobs={study.job_id}",
            f"--name={study.name}",
            "--format=JobID,JobName,State",
            "--parsable2",
            "--delimiter=,",
            "--noheader",
        ]
        command = " ".join(shlex.quote(arg) for arg in args)

        # noinspection SpellCheckingInspection
        def execute_command_mock(cmd: str):
            if cmd == f"scontrol show job {study.job_id}":
                return "", "Invalid job id specified"
            if cmd == command:
                return f"{study.job_id},{study.name},{job_state}", None
            assert False, f"Unknown command: {cmd}"

        remote_env.connection.execute_command = execute_command_mock
        actual = remote_env.get_job_state_flags(study)
        assert actual == (True, False, False)

    # noinspection SpellCheckingInspection
    @pytest.mark.unit_test
    def test_get_job_state_flags__scontrol_nominal(self, remote_env, study):
        study.job_id = 42
        job_state = "RUNNING"
        output, error = f"JobState={job_state}", None
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        actual = remote_env.get_job_state_flags(study)
        assert actual == (True, False, False)

    # noinspection SpellCheckingInspection
    @pytest.mark.unit_test
    def test_get_job_state_flags__scontrol_non_parsable(self, remote_env, study):
        study.job_id = 42
        output, error = "Blah!Blah!", None
        remote_env.connection.execute_command = mock.Mock(return_value=(output, error))
        with pytest.raises(GetJobStateError, match="non-parsable output") as ctx:
            remote_env.get_job_state_flags(study)
        assert output in str(ctx.value)
        command = f"scontrol show job {study.job_id}"
        remote_env.connection.execute_command.assert_called_once_with(command)

    @pytest.mark.unit_test
    def test_get_job_state_flags__sacct_bad_output(self, remote_env, study):
        study.job_id = 42
        args = [
            "sacct",
            f"--jobs={study.job_id}",
            f"--name={study.name}",
            "--format=JobID,JobName,State",
            "--parsable2",
            "--delimiter=,",
            "--noheader",
        ]
        command = " ".join(shlex.quote(arg) for arg in args)

        # the output of `sacct` is not: JobID,JobName,State
        output = "the sun is shining"

        # noinspection SpellCheckingInspection
        def execute_command_mock(cmd: str):
            if cmd == f"scontrol show job {study.job_id}":
                return "", "Invalid job id specified"
            if cmd == command:
                return output, None
            assert False, f"Unknown command: {cmd}"

        remote_env.connection.execute_command = execute_command_mock

        with pytest.raises(GetJobStateError, match="non-parsable output") as ctx:
            remote_env.get_job_state_flags(study)
        assert output in str(ctx.value)

    # noinspection SpellCheckingInspection
    @pytest.mark.unit_test
    def test_get_job_state_flags__sacct_call_fails(self, remote_env, study):
        study.job_id = 42
        args = [
            "sacct",
            f"--jobs={study.job_id}",
            f"--name={study.name}",
            "--format=JobID,JobName,State",
            "--parsable2",
            "--delimiter=,",
            "--noheader",
        ]
        command = " ".join(shlex.quote(arg) for arg in args)

        # noinspection SpellCheckingInspection
        def execute_command_mock(cmd: str):
            if cmd == f"scontrol show job {study.job_id}":
                return "", "Invalid job id specified"
            if cmd == command:
                return None, "an error occurs"
            assert False, f"Unknown command: {cmd}"

        remote_env.connection.execute_command = execute_command_mock
        with pytest.raises(GetJobStateError, match="an error occurs"):
            remote_env.get_job_state_flags(study, attempts=2, sleep_time=0.1)
        remote_env.connection.execute_command.mock_calls = [
            call(command),
            call(command),
        ]

    @pytest.mark.unit_test
    @pytest.mark.parametrize(
        "state, expected",
        [
            pytest.param("", (True, False, False), id="unknown-means-RUNNING"),
            ("PENDING", (False, False, False)),
            ("RUNNING", (True, False, False)),
            ("CANCELLED", (True, True, True)),
            ("CANCELLED by 123456", (True, True, True)),
            ("TIMEOUT", (True, True, True)),
            ("COMPLETED", (True, True, False)),
            ("FAILED", (True, True, True)),
        ],
    )
    def test_get_job_state_flags__sacct_nominal_case(
        self, remote_env, study, state, expected
    ):
        """
        Check that the "get_job_state_flags" method is correctly returning
        the status flags ("started", "finished", and "with_error")
        for a SLURM job in a specific state.
        """
        study.job_id = 42
        args = [
            "sacct",
            f"--jobs={study.job_id}",
            f"--name={study.name}",
            "--format=JobID,JobName,State",
            "--parsable2",
            "--delimiter=,",
            "--noheader",
        ]
        command = " ".join(shlex.quote(arg) for arg in args)

        # noinspection SpellCheckingInspection
        def execute_command_mock(cmd: str):
            if cmd == f"scontrol show job {study.job_id}":
                return "", "Invalid job id specified"
            if cmd == command:
                # the output of `sacct` should be: JobID,JobName,State
                output = f"{study.job_id},{study.name},{state}" if state else ""
                return output, None
            assert False, f"Unknown command: {cmd}"

        remote_env.connection.execute_command = execute_command_mock

        actual = remote_env.get_job_state_flags(study)
        assert actual == expected

    @pytest.mark.unit_test
    def test_given_a_not_started_study_when_list_remote_logs_is_called_then_returns_empty_list(
        self, remote_env, study
    ):
        # given
        study.started = False
        remote_env.connection.execute_command = mock.Mock(return_value=("", ""))

        # when
        output = remote_env._list_remote_logs(study)

        # then
        assert output == []

    @pytest.mark.unit_test
    def test_given_a_started_study_when_list_remote_logs_is_called_then_connection_execute_command_is_called_with_right_argument(
        self, remote_env, study
    ):
        # given
        study.job_id = 24
        study.started = True
        remote_env.connection.execute_command = mock.Mock(return_value=("", ""))
        command = f"ls  {remote_env.remote_base_path}/*{study.job_id}*.txt"

        # when
        remote_env._list_remote_logs(study.job_id)

        # then
        remote_env.connection.execute_command.assert_called_once_with(command)

    @pytest.mark.unit_test
    def test_given_a_started_study_when_list_remote_logs_is_called_and_execute_command_produces_error_then_returns_empty_list(
        self, remote_env, study
    ):
        # given
        study.started = True
        remote_env.connection.execute_command = mock.Mock(
            return_value=("output", "error")
        )

        # when
        output = remote_env._list_remote_logs(study)

        # then
        assert output == []

    @pytest.mark.unit_test
    def test_given_a_started_study_when_list_remote_logs_is_called_and_execute_command_produces_no_output_then_returns_empty_list(
        self, remote_env, study
    ):
        # given
        study.started = True
        remote_env.connection.execute_command = mock.Mock(return_value=("", ""))

        # when
        output = remote_env._list_remote_logs(study)

        # then
        assert output == []

    @pytest.mark.unit_test
    def test_given_a_started_study_when_list_remote_logs_is_called_then_returns_not_empty_list(
        self, remote_env, study
    ):
        # given
        study.started = True
        remote_env.connection.execute_command = mock.Mock(return_value=("output", ""))

        # when
        output = remote_env._list_remote_logs(study)

        # then
        assert output

    @pytest.mark.unit_test
    def test_given_a_study_when_download_logs_is_called_then_list_remote_logs_is_called(
        self, remote_env, study
    ):
        # given
        remote_env._list_remote_logs = mock.Mock(return_value=[])

        # when
        remote_env.download_logs(study)

        # then
        remote_env._list_remote_logs.assert_called_once_with(study.job_id)

    @pytest.mark.unit_test
    def test_given_an_empty_file_list_when_download_logs_is_called_then_connection_download_files_is_not_called(
        self, remote_env, study
    ):
        # given
        remote_env._list_remote_logs = mock.Mock(return_value=[])
        remote_env.connection.download_file = mock.Mock()

        # when
        return_flag = remote_env.download_logs(study)

        # then
        remote_env.connection.download_file.assert_not_called()
        assert return_flag is False

    @pytest.mark.unit_test
    def test_given_a_file_list_when_download_logs_is_called_then_connection_download_files_is_called_with_correct_arguments(
        self, remote_env, study
    ):
        # given
        study.job_log_dir = "job_log_dir"
        file_path = "file"
        remote_env._list_remote_logs = mock.Mock(return_value=[file_path])
        remote_env.connection.download_file = mock.Mock()

        src = f"{remote_env.remote_base_path}/{file_path}"
        dst = str(Path(study.job_log_dir) / file_path)

        # when
        remote_env.download_logs(study)

        # then
        remote_env.connection.download_file.assert_called_once_with(src, dst)

    @pytest.mark.unit_test
    def test_given_a_not_clean_study_and_a_file_list_with_two_elements_when_download_logs_is_called_then_connection_download_files_is_called_twice(
        self, remote_env, study
    ):
        # given
        study.remote_server_is_clean = False
        study.job_log_dir = "job_log_dir"
        remote_env._list_remote_logs = mock.Mock(
            return_value=["file_path", "file_path2"]
        )
        remote_env.connection.download_file = mock.Mock(return_value=True)

        # when
        return_flag = remote_env.download_logs(study)

        # then
        remote_env.connection.download_file.assert_called()
        assert remote_env.connection.download_file.call_count == 2
        assert return_flag is True

    @pytest.mark.unit_test
    def test_given_a_not_finished_study_when_check_final_zip_not_empty_then_returns_false(
        self, remote_env, study
    ):
        # given
        study.finished = False
        final_zip_name = "final_zip_name"
        # when
        return_flag = remote_env.check_final_zip_not_empty(study, final_zip_name)
        # then
        assert return_flag is False

    @pytest.mark.unit_test
    def test_given_a_finished_study_when_check_final_zip_not_empty_then_check_file_not_empty_is_called(
        self, remote_env, study
    ):
        # given
        study.finished = True
        final_zip_name = "final_zip_name"
        remote_env.connection.check_file_not_empty = mock.Mock()
        # when
        remote_env.check_final_zip_not_empty(study, final_zip_name)
        # then
        remote_env.connection.check_file_not_empty.assert_called_once()

    @pytest.mark.unit_test
    def test_given_a_finished_study_with_empty_file_when_check_final_zip_not_empty_then_return_false(
        self, remote_env, study
    ):
        # given
        study.finished = True
        final_zip_name = "final_zip_name"
        remote_env.connection.check_file_not_empty = mock.Mock(return_value=False)
        # when
        return_flag = remote_env.check_final_zip_not_empty(study, final_zip_name)
        # then
        assert return_flag is False

    @pytest.mark.unit_test
    def test_given_a_finished_study_with_not_empty_file_when_check_final_zip_not_empty_then_return_true(
        self, remote_env, study
    ):
        # given
        study.finished = True
        final_zip_name = "final_zip_name"
        remote_env.connection.check_file_not_empty = mock.Mock(return_value=True)
        # when
        return_flag = remote_env.check_final_zip_not_empty(study, final_zip_name)
        # then
        assert return_flag is True

    @pytest.mark.unit_test
    def test_given_a_study_when_download_final_zip_is_called_then_check_final_zip_not_empty_is_called_with_correct_argument(
        self, remote_env, study
    ):
        # given
        study.path = "path"
        study.job_id = 1234
        final_zip_name = f"finished_{study.name}_{study.job_id}.zip"
        remote_env.check_final_zip_not_empty = mock.Mock()
        # when
        remote_env.download_final_zip(study)
        # then
        remote_env.check_final_zip_not_empty.assert_called_once_with(
            study, final_zip_name
        )

    @pytest.mark.unit_test
    def test_given_a_study_with_empty_final_zip_when_download_final_zip_is_called_then_return_none(
        self, study, remote_env
    ):
        # given
        study.path = "path"
        study.job_id = 1234
        remote_env.connection.check_file_not_empty = mock.Mock(return_value=False)
        # when
        return_value = remote_env.download_final_zip(study)
        # then
        assert return_value is None

    @pytest.mark.unit_test
    def test_given_a_study_with_final_zip_already_downloaded_when_download_final_zip_is_called_then_return_local_final_zipfile_path(
        self, study, remote_env
    ):
        # given
        study.path = "path"
        study.job_id = 1234
        study.local_final_zipfile_path = "local_final_zipfile_path"
        remote_env.check_final_zip_not_empty = mock.Mock(return_value=True)
        # when
        return_value = remote_env.download_final_zip(study)
        # then
        assert return_value == study.local_final_zipfile_path

    @pytest.mark.unit_test
    def test_given_a_study_with_final_zip_when_download_final_zip_is_called_then_download_file_is_called_with_correct_argument(
        self, study, remote_env
    ):
        # given
        study.finished = True
        study.job_id = 1234
        study.local_final_zipfile_path = ""
        final_zip_name = f"finished_{Path(study.path).name}_{study.job_id}.zip"
        remote_env.connection.check_file_not_empty = mock.Mock(return_value=True)
        remote_env.connection.download_file = mock.Mock()
        local_final_zipfile_path = str(Path(study.output_dir) / final_zip_name)
        src = f"{remote_env.remote_base_path}/{final_zip_name}"
        dst = local_final_zipfile_path
        # when
        remote_env.download_final_zip(study)
        # then
        remote_env.connection.download_file.assert_called_once_with(src, dst)

    @pytest.mark.unit_test
    def test_given_a_study_with_final_zip_when_download_final_zip_is_called_and_file_is_not_downloaded_then_returns_none(
        self, study, remote_env
    ):
        # given
        study.path = "path"
        study.job_id = 1234
        study.local_final_zipfile_path = ""
        remote_env.check_file_not_empty = mock.Mock(return_value=True)
        remote_env.connection.download_file = mock.Mock(return_value=False)
        # when
        return_value = remote_env.download_final_zip(study)
        # then
        assert return_value is None

    @pytest.mark.unit_test
    def test_given_a_study_with_final_zip_when_download_final_zip_is_called_and_file_is_downloaded_then_returns_local_zipfile_path(
        self, study, remote_env
    ):
        # given
        study.finished = True
        study.job_id = 1234
        final_zip_name = f"finished_{Path(study.path).name}_{study.job_id}.zip"
        local_final_zipfile_path = str(Path(study.output_dir) / final_zip_name)
        study.local_final_zipfile_path = ""
        remote_env.connection.check_file_not_empty = mock.Mock(return_value=True)
        remote_env.connection.download_file = mock.Mock(return_value=True)
        # when
        return_value = remote_env.download_final_zip(study)
        # then
        assert return_value == local_final_zipfile_path

    @pytest.mark.unit_test
    def test_given_a_study_with_input_zipfile_removed_when_remove_input_zipfile_then_return_true(
        self, remote_env, study
    ):
        # given
        study.input_zipfile_removed = True
        # when
        output = remote_env.remove_input_zipfile(study)
        # then
        assert output is True

    @pytest.mark.unit_test
    def test_given_a_study_when_remove_input_zipfile_then_connection_remove_file_is_called(
        self, remote_env, study
    ):
        # given
        study.input_zipfile_removed = False
        study.zipfile_path = "zipfile_path"
        zip_name = Path(study.zipfile_path).name
        command = f"{remote_env.remote_base_path}/{zip_name}"
        # when
        remote_env.remove_input_zipfile(study)
        # then
        # noinspection PyUnresolvedReferences
        remote_env.connection.remove_file.assert_called_once_with(command)

    @pytest.mark.unit_test
    def test_given_a_study_when_input_zipfile_not_removed_and_connection_successfully_removed_file_then_return_true(
        self, remote_env, study
    ):
        # given
        study.input_zipfile_removed = False
        study.zipfile_path = "zipfile_path"
        remote_env.connection.remove_file = mock.Mock(return_value=True)
        # when
        output = remote_env.remove_input_zipfile(study)
        # then
        assert output is True

    @pytest.mark.unit_test
    def test_given_a_study_when_remove_remote_final_zipfile_then_connection_remove_file_is_called(
        self, remote_env, study
    ):
        # given
        study.input_zipfile_removed = False
        study.zipfile_path = "zipfile_path"
        command = (
            f"{remote_env.remote_base_path}/{Path(study.local_final_zipfile_path).name}"
        )
        remote_env.connection.execute_command = mock.Mock(return_value=("", ""))
        # when
        remote_env.remove_remote_final_zipfile(study)
        # then
        # noinspection PyUnresolvedReferences
        remote_env.connection.remove_file.assert_called_once_with(command)

    @pytest.mark.unit_test
    def test_given_a_study_with_clean_remote_server_when_clean_remote_server_called_then_return_false(
        self, remote_env, study
    ):
        # given
        study.remote_server_is_clean = True
        # when
        output = remote_env.clean_remote_server(study)
        # then
        assert output is False

    @pytest.mark.unit_test
    def test_given_a_study_when_clean_remote_server_called_then_remove_zip_methods_are_called(
        self, remote_env, study
    ):
        # given
        study.remote_server_is_clean = False
        remote_env.remove_remote_final_zipfile = mock.Mock(return_value=False)
        remote_env.remove_input_zipfile = mock.Mock(return_value=False)
        # when
        remote_env.clean_remote_server(study)
        # then
        remote_env.remove_remote_final_zipfile.assert_called_once_with(study)
        remote_env.remove_input_zipfile.assert_called_once_with(study)

    @pytest.mark.unit_test
    def test_given_a_study_when_clean_remote_server_called_then_return_correct_result(
        self, remote_env, study
    ):
        # given
        study.remote_server_is_clean = False
        remote_env.remove_remote_final_zipfile = mock.Mock(return_value=False)
        remote_env.remove_input_zipfile = mock.Mock(return_value=False)
        # when
        output = remote_env.clean_remote_server(study)
        # then
        assert output is False
        # given
        study.remote_server_is_clean = False
        remote_env.remove_remote_final_zipfile = mock.Mock(return_value=True)
        remote_env.remove_input_zipfile = mock.Mock(return_value=False)
        # when
        output = remote_env.clean_remote_server(study)
        # then
        assert output is False
        # given
        study.remote_server_is_clean = False
        remote_env.remove_remote_final_zipfile = mock.Mock(return_value=False)
        remote_env.remove_input_zipfile = mock.Mock(return_value=True)
        # when
        output = remote_env.clean_remote_server(study)
        # then
        assert output is False
        # given
        study.remote_server_is_clean = False
        remote_env.remove_remote_final_zipfile = mock.Mock(return_value=True)
        remote_env.remove_input_zipfile = mock.Mock(return_value=True)
        # when
        output = remote_env.clean_remote_server(study)
        # then
        assert output is True

    @pytest.mark.unit_test
    def test_given_time_limit_lower_than_min_duration_when_convert_time_is_called_return_min_duration(
        self,
    ):
        # given
        time_lim_sec = 42
        # when
        output = RemoteEnvironmentWithSlurm.convert_time_limit_from_seconds_to_minutes(
            time_lim_sec
        )
        # then
        assert output == 1

    @pytest.mark.parametrize(
        "job_type,mode,post_processing",
        [
            ("ANTARES_XPANSION_R", Modes.xpansion_r, True),
            ("ANTARES_XPANSION_CPP", Modes.xpansion_cpp, True),
            ("ANTARES", Modes.antares, True),
            ("ANTARES_XPANSION_R", Modes.xpansion_r, False),
            ("ANTARES_XPANSION_CPP", Modes.xpansion_cpp, False),
            ("ANTARES", Modes.antares, False),
        ],
    )
    @pytest.mark.unit_test
    def test_compose_launch_command(
        self,
        remote_env,
        job_type,
        mode,
        post_processing,
        study,
    ):
        # given
        filename_launch_script = remote_env.slurm_script_features.solver_script_path
        # when
        study.run_mode = mode
        study.post_processing = post_processing
        script_params = ScriptParametersDTO(
            study_dir_name=Path(study.path).name,
            input_zipfile_name=Path(study.zipfile_path).name,
            time_limit=1,
            n_cpu=study.n_cpu,
            antares_version=int(study.antares_version),
            run_mode=study.run_mode,
            post_processing=study.post_processing,
            other_options="",
        )
        command = remote_env.compose_launch_command(script_params)
        # then
        change_dir = f"cd {remote_env.remote_base_path}"
        reference_submit_command = (
            f"sbatch"
            f' --job-name="{Path(study.path).name}"'
            f" --time={study.time_limit // 60}"
            f" --cpus-per-task={study.n_cpu}"
            f" {filename_launch_script}"
            f' "{Path(study.zipfile_path).name}"'
            f" {study.antares_version}"
            f" {job_type}"
            f" {post_processing}"
            f" ''"
        )
        reference_command = f"{change_dir} && {reference_submit_command}"
        assert command.split() == reference_command.split()
        assert command == reference_command
