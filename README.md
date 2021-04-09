### Sango UI Automation Testing tool

```bash
$ cp .env.example .env
# Change TARGET_PROJECT_DIR on .env file

$ cp docker/target/Dockerfile <YOUR-PROJECT-DIR>/Dockerfile.autotest
```

### Add your test


- `$ mkdir automation-ui-testcases` on `YOUR-PROJECT-DIR`
- `ln -s YOUR-PROJECT-DIR/automation-ui-testcases ./testcases`
- Create your test case on `automation-ui-testcases/test_*.py`

Sample test code

```
from .base import BaseTestCase


class TestPageNotFound(BaseTestCase):
    def test_valid_element(self):
        self.assertEqual(1, 1)

    def test_valid_background_color(self):
        self.assertEqual(1, 1)

```

### RUN

```bash
$ make test


# Fast write testcase, no need build container again
$ make test-nobuild
```
