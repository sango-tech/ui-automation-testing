import os
import logging
import unittest
from urllib.parse import urljoin
from selenium import webdriver

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class BaseTestCase(unittest.TestCase):
    DEVICE_SP = "sp"
    DEVICE_TABLET = "tablet"
    DEVICE_DESKTOP = "desktop"

    target_device = DEVICE_DESKTOP

    # target-project:80 is a service on docker-compose.yml
    # TARGET_PROJECT_URL only using for extra target project
    base_url = os.environ.get("TARGET_PROJECT_URL", "http://target-project:80")
    driver = None

    @classmethod
    def setUp(self):
        assert(self.base_url is not None)

    def set_device(self, device):
        self.target_device = device

    def get_url(self, subpath=""):
        return urljoin(self.base_url, subpath)

    def get_device_emulation(self):
        if self.target_device == "sp":
            return {
                "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"  # noqa
            }

        if self.target_device == "tablet":
            return {
                "deviceMetrics": {"width": 980, "height": 1208, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"  # noqa
            }

        return {
            "deviceMetrics": {"width": 1025, "height": 1208, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0"
        }

    def set_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--ignore-ssl-errors=yes')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_experimental_option("mobileEmulation", self.get_device_emulation())

        self.driver = webdriver.Remote(self.selenium_hub(), desired_capabilities=chrome_options.to_capabilities())
        return self.driver

    def selenium_hub(self):
        return "http://selenium-hub:4444/wd/hub"

    @classmethod
    def tearDown(self):
        if self.driver:
            self.driver.quit()
