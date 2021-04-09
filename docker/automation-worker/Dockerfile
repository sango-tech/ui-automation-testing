FROM python:3.7

# Target testing directory (i.e /usr/home/my-vuejs-project)
ARG TARGET_PROJECT_DIR

WORKDIR /sango
ADD docker/automation-worker/requirements.txt /usr/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /usr/requirements.txt

COPY . .
COPY ${TARGET_PROJECT_DIR}/automation-ui-testcases/test_*.py ./testcases

RUN useradd -ms /bin/bash sango
RUN chown -R sango:sango /sango
RUN chmod 755 /sango
USER sango

RUN chmod +x scripts/run_unittest.sh
RUN chmod +x scripts/wait-for-it.sh
