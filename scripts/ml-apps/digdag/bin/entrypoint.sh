#!/usr/bin/env bash

# set bash options
set -ex

# rendering server.properties
envsubst < /app/scheduler/conf/server.properties > /app/scheduler/conf/server.properties

# rendering pgpass file
echo "$POSTGRES_HOST:$POSTGRES_PORT:$POSTGRES_DB:$POSTGRES_USER:$POSTGRES_PASSWORD" > ~/.pgpass
chmod 600 ~/.pgpass

# run digdag server
digdag server --config /app/scheduler/conf/server.properties
