FROM ml-apps-common

# Make workspace
RUN mkdir -p /app/notebook
WORKDIR /app/notebook

# Install packages
COPY jupyter/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Run jupyter server
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
