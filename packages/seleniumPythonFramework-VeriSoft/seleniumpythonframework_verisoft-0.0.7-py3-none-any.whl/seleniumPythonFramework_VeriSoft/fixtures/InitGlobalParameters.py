import datetime
import logging.config
import yaml
import pytest
import json
import os

"""
Init global parameters fixture function to load all the project necessary global parameters before all the tests running.

@Author: Efrat Cohen
@Date: 11.2022
"""


def before_all():
    """
    Loads project global parameters and store them as pytest global variable, so the parameters will be accessible
    everywhere
    """

    # Get the path of the file that is using your package
    package_path = os.path.dirname(os.path.abspath(__file__))

    # Get the path of the file you want to access (assuming it is in the same directory)
    file_path = os.path.join(package_path, 'app-config.json')

    # Init Json properties
    # Opening JSON file
    f = open(file_path)
    # Returns JSON object as a dictionary
    data = json.load(f)
    # Store the properties in pytest global variables
    pytest.properties = data
    # Closing file
    f.close()

    # Init Tokens JSON data
    # Opening token JSON file
    f = open(pytest.project_dir + "/testsData/tokens.json")
    # Returns JSON object as a dictionary
    tokens = json.load(f)
    # Store the data in pytest global variables
    pytest.tokens = tokens
    # Closing file
    f.close()

    # Init farms JSON data
    # Opening token JSON file
    f = open(pytest.project_dir + "/testsData/farms.json")
    # Returns JSON object as a dictionary
    farms_data = json.load(f)
    # Store the data in pytest global variables
    pytest.farms_data = farms_data
    # Closing file
    f.close()

    # Init wallets JSON data
    # Opening token JSON file
    f = open(pytest.project_dir + "/testsData/wallets.json")
    # Returns JSON object as a dictionary
    wallets_data = json.load(f)
    # Store the data in pytest global variables
    pytest.wallets_data = wallets_data
    # Closing file
    f.close()

    # Initialize the logger instance.
    with open(pytest.project_dir + "/Tests/logging.yaml", 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

    # Get an instance of the logger and use it to write a log
    # Store the logger in pytest global variables
    pytest.logger = logging.getLogger(__name__)


def get_current_datetime():
    """
    init current datetime
    @return date_time - current time
    """
    # Current date and time
    current_time = datetime.datetime.now()
    date_time = current_time.strftime("%d-%m-%Y %H-%M-%S")
    return date_time
