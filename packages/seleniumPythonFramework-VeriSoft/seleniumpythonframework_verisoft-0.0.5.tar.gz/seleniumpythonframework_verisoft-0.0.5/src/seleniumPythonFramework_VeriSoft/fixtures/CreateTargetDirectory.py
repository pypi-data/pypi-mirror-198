import os
from os.path import dirname
import pytest
from pathlib import Path
"""
creates target directory with necessary folders for the files created out of the build.

@Author: Efrat Cohen
@Date: 12.2022
"""


def before_all():
    """
    check if target directory exist, if not - create this directory with screenshots folder in.
    """
    # Get project path
    infra_project_path = dirname(dirname(__file__))
    tests_project_path = str(Path(__file__).parent.parent.parent) + '/automation-qa-tests-tokensfarm'

    # Store the project user directory in pytest global variables
    pytest.project_dir = tests_project_path
    pytest.user_dir = infra_project_path

    # Specify path
    path = tests_project_path + "/target"

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        # Create target directory
        os.makedirs(tests_project_path + "/target", exist_ok=True)

        # Create screenshots folder in target directory
        os.makedirs(tests_project_path + "/target/screenshots", exist_ok=True)

