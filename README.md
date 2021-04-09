### Sango UI Automation Testing tool

Automation UI test is combined from Selenium + Python Unit test. This help you can set your testing scenario.
This tool is writing by Python and Docker compose.

### Run your app

Run your webapp first, then check your local IP if you are on local. Or directly testing on a live webapp (e.i https://my-live-website.com).


In case locally

```bash
# Get your local IP to make sure selenium can read your website from inside docker container
$ ifconfig

# .env file
TARGET_PROJECT_URL=https://192.168.1.181:8081

```

### Get started

```bash
$ cp .env.example .env
```

### Add your test

- `$ mkdir automation-ui-testcases` on `YOUR-PROJECT-DIR`
- `ln -s YOUR-PROJECT-DIR/automation-ui-testcases ./testcases`
- Create your test case on following this structor `automation-ui-testcases/test_*.py`


### Sample test code

```
from base import BaseTestCase
from selenium.common.exceptions import NoSuchElementException


class TestPageNotFound(BaseTestCase):
    def test_valid_element(self):
        self.set_device(self.DEVICE_DESKTOP)
        driver = self.set_driver()

        # This auto generate to https://192.168.1.181:8081/not-found
        target_url = self.get_url("not-found")
        driver.get(target_url)
        # driver.implicitly_wait(3)

        try:
            logo_src = driver.find_element_by_css_selector(".app-logo").get_attribute("src")
            self.assertIn("logo", logo_src)

            h1_text = driver.find_element_by_css_selector("h1").text
            self.assertEqual(h1_text, "404")
        except NoSuchElementException as e:
            self.fail(e)

```
### Run test

```bash
$ make test
```
