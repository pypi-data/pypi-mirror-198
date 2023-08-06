import pytest
from src.seleniumPythonFramework_VeriSoft.drivers import ChromeDriver, BraveDriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from src.seleniumPythonFramework_VeriSoft.infra.CustomEventListener import CustomEventListener

"""
setup and cleanup fixtures functions to init and close the driver. 
before the tests - init the driver, after the tests - close driver.

@Author: Efrat Cohen
@Date: 10.2022
"""


def before_test(request):
    pytest.logger.info("Test: " + request.node.nodeid + " is started ")

    # Init driver based on injected driver type
    if pytest.data_driven.get("browser") == "chrome":
        pytest.logger.info("chrome driver type injected, initialize chrome browser")
        driver = ChromeDriver.initChromeDriver()
    elif pytest.data_driven.get("browser") == "brave":
        pytest.logger.info("brave browser type injected, initialize brave browser")
        driver = BraveDriver.initBraveDriver()
    # If no driver type injected - chrome is the default
    else:
        pytest.logger.info("no browser type injected, initialize default chrome browser")
        driver = ChromeDriver.initChromeDriver()

    # Add event listener
    event_listener = CustomEventListener()
    event_firing_driver = EventFiringWebDriver(driver, event_listener)

    pytest.logger.info("driver :" + event_firing_driver.name + " had installed successfully")
    event_firing_driver.maximize_window()
    pytest.logger.info("window had maximize")

    # Store driver in cls object
    request.cls.driver = event_firing_driver
    pytest.driver = event_firing_driver


# Use in cleanup fixture
def after_test(request):
    pytest.logger.info("close " + request.cls.driver.name + "driver")
    request.cls.driver.quit()
    pytest.logger.info("Test " + request.node.nodeid + " is Finished")
