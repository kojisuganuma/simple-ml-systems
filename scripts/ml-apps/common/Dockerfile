FROM python:3.6.5

# Make workspace
RUN mkdir -p /app/common

# Install packages
COPY common/requirements.txt /tmp/requirements_common.txt
RUN pip install -r /tmp/requirements_common.txt
