FROM python:3.6.5

# install packages
RUN pip install future

# Make workspace
RUN mkdir -p /app/python

# Copy src
COPY src /app/python

# run command
CMD ["python", "/app/python/main.py"]
