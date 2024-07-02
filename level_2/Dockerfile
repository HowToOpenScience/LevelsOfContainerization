# Choose the base image
FROM python:3.11.9-bookworm

# Set the environment variable
ENV TEST_VAR="Hello world!"

# Run commands
RUN mkdir /test && echo ${TEST_VAR} > /test/example.txt

# Change the working directory
WORKDIR /src
