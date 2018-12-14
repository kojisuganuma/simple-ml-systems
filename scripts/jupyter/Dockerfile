FROM python:3.6.5

# Make workspace
RUN mkdir -p /app/notebook
WORKDIR /app/notebook

# Install packages
COPY requirements.txt /tmp/requirements_jupyter.txt
RUN pip install -r /tmp/requirements_jupyter.txt

# Run jupyter server
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
