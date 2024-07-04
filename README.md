# Levels of Containerization

Levels of Containerization is an example explaining the different levels of complexity when sharing materials. Each level contains its own README with what they represent. This is meant as an aid for understanding how to make materials more usable by others in a simple manner.

**All examples are shown in Python, as it is the most common language used across previous proceedings in this conference. However, the concepts can easily be transposed to other languages.**

## Setup

This work contains a development container that contains everything you may need. The container can be opened in Visual Studio Code for ease of convenience. Follow any addittional instructions within the README of each folder to get every level setup. You will need be logged in to Docker to use this configuration as `docker-in-docker` is used to emulated creating a docker container. This can be done in Docker Desktop or through the `docker login` cli. The development container is loaded if the text in the terminal says 'Done. Press any key to close the terminal.'

If done manually, this project uses Python 3.12.4, R 4.4, Docker, and Development Containers to setup the process. The level setups are written for bash in Linux; however, links to other operating systems or resources are provided when necessary.

## Disclaimer

This will not make materials completely reproducible. Docker containers, while taggable, do not maintain previous versions, meaning that any changes effect the container as a whole. Some containers are also deleted, such as nvidia's for CUDA, making reproducibility not always possible. The following information is only a tool to help mitigate issues when other people are trying to view and use your work.
