# syntax = docker/dockerfile:1.0-experimental

# We are going to do this build in a multi-stage approach in order to 1.
#   1. Protect secrets required as env variables during the build process from being
#      embedded in the resuting image
#   2. Reduce the resulting image size by removing unnecessary build tools.

# The overall approach employed here is inspired by the following article:
#   https://pythonspeed.com/articles/multi-stage-docker-python/
# We are using solution 2.

# BUILD IMAGE ##########################
# We could push the build size down more by using "alpine", but as many service
# libs make use of gcc, where alpine use muscl. we consider it safer to eat the 25% size
# for the confidence of using the C-comiler most dependencies are built for.
FROM python:3.8-slim AS builder

# Use PIP_INDEX_URL and PIP_EXTRA_INDEX_URL from the build environment. These may
# contains Access tokens for private repos so we need to not let them into the
# final build of the service.
ARG PIP_INDEX_URL
ARG PIP_EXTRA_INDEX_URL

ENV PIP_INDEX_URL=$PIP_INDEX_URL
ENV PIP_EXTRA_INDEX_URL=$PIP_EXTRA_INDEX_URL

# Set the virtual env.
ENV VIRTUAL_ENV=/opt/venv
# Create a virtual env.
RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Make /app the work directory
WORKDIR /app

# Copy the current directory (containing the full source code for the service) into the
# container at /app.
COPY . /app

# The virtual environment is set in the base image so we don't neeed to worry about
# setting it

# Add dependencies for building wheels.
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

# Install the app (pip and setuptools are upgraded in the base image).
RUN pip install --no-cache-dir .

# SERVICE IMAGE ##########################
# We are done installing and building the app, now we need to make the actual service
# container.
FROM python:3.8-slim AS service

# Copy our virtual environment from the previous build.
COPY --from=builder /opt/venv /opt/venv

# Set the virtual env
ENV VIRTUAL_ENV=/opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
# Make sure we use the virtualenv:
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Set the working directory to /app
WORKDIR /app

# Copy ONLY the /directories in the app we need to run it, without getting bogged down
# by development files.
COPY service/. /app/stalkreports
COPY service/. /app/gen
COPY service/. /app/stalk_proto

# Make port 50051 available to the world outside this container for the grpc connection.
EXPOSE 50051

# Run service when the container launches
CMD ["python", "stalkreports"]
