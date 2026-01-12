
import pytest, subprocess, time
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture
def driver():
    subprocess.run(
        ["adb", "shell", "monkey", "-p", "com.adidas.app",
         "-c", "android.intent.category.LAUNCHER", "1"],
        capture_output=True
    )

    time.sleep(4)

    options = UiAutomator2Options()
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.no_reset = True
    options.new_command_timeout = 300

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()
