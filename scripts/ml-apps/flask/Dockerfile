FROM ml-apps-common

# Make workspace
RUN mkdir -p /app/api

# Copy src
COPY flask/src /app/api

# Install packages
COPY flask/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

CMD ["python", "/app/api/run.py"]
