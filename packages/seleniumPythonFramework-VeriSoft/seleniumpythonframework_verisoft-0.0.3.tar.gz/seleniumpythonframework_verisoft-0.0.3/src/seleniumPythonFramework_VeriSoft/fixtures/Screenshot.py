import pytest
from fixtures.InitGlobalParameters import get_current_datetime

"""
screenshots fixture function for screenshot of the test falling
after each test, if the test failed - take screenshot and store him with datetime

@Author: Efrat Cohen
@Date: 09.2022
"""


def after_test(request):
    """
    Take screenshot when test fail, save it in screenshot folder with current datetime in file name
    :param request: the requesting test context
    """
    if request.session.testsfailed:
        pytest.logger.info("test " + request.node.nodeid + " failed, take screenshot")
        # Get driver name
        driver_type = request.cls.driver.name
        # Save screenshot in target directory
        request.cls.driver.save_screenshot(pytest.project_dir + '/target/screenshots/' + "SC " + get_current_datetime() + " " + driver_type + ".png")
        pytest.logger.info("screenshot successfully taken")