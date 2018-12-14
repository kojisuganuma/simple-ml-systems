FROM openjdk:8-jdk

# Install some packages
RUN apt-get update && \
    apt-get install -y curl gettext-base postgresql-client

# Install docker client
RUN curl -fsSL https://get.docker.com/builds/Linux/x86_64/docker-1.13.1.tgz \
    | tar -xzC /usr/local/bin --strip=1 docker/docker

# Installing digdag
RUN curl -o /usr/local/bin/digdag --create-dirs -L "http://dl.digdag.io/digdag-latest" && \
    chmod +x /usr/local/bin/digdag

# Make workspace
RUN mkdir -p /app/scheduler/bin \
    mkdir -p /app/scheduler/conf \
    mkdir -p /app/scheduler/projects
COPY digdag/bin/entrypoint.sh /app/scheduler/bin
COPY digdag/conf/server.properties /app/scheduler/conf
RUN chmod +x /app/scheduler/bin/entrypoint.sh

# Set envs
ENV DIGDAG_BIND="0.0.0.0" \
    DIGDAG_PORT=65432 \
    DIGDAG_ADMIN_BIND="0.0.0.0" \
    DIGDAG_ADMIN_PORT=65433 \
    DIGDAG_ACCESS_LOG_PATTERN=json \
    POSTGRES_TYPE=postgresql \
    POSTGRES_HOST=postgresql \
    POSTGRES_PORT=5432 \
    POSTGRES_USER=digdag \
    POSTGRES_PASSWORD=digdag \
    POSTGRES_DB=digdag

# Run scheduler
ENTRYPOINT ["/app/scheduler/bin/entrypoint.sh"]
