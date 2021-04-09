FROM python:3.7

WORKDIR /sango
ADD docker/automation-worker/requirements.txt /usr/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /usr/requirements.txt

COPY . .

RUN useradd -ms /bin/bash sango
RUN chown -R sango:sango /sango
RUN chmod 755 /sango
USER sango

RUN chmod +x scripts/run_unittest.sh
RUN chmod +x scripts/wait-for-it.sh
