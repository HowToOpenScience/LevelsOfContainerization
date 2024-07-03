# Level 2: Docker Containers

Level 2 contains an example of Docker containers: isolated environments to run some application. A container, for most instances, guarantees that the codebase will be able to run on another machine, as the definition of how to set up the machine will be provided within the image itself.

## What are Docker Containers?

Containers are lightweight, standalone, isolated environment to run some application. The end result is similar to a virtual machine, although with different reasons and approaches. A container is built off of some image (e.g. usually a Linux operating system) that can have additional commands applied during setup to create the environment.

A container can be used to essentially ship an environment to other users that is more or less guaranteed to run, provided any non-automated proccesses are defined within the provided README. It forces everything that is necessary on the machine to be installed into the container. It is also a good method to see whether you have made any assumptions about what your materials need to run on another machine. As everything is run within Linux, there should be minor differences in operating, as most implementations of research in education technology do not operate on a low enough level.

## Setting up a Docker Container (the Dockerfile)

A Docker container is created based upon an image constructed from a [`Dockerfile`](https://docs.docker.com/reference/dockerfile/). The following commands are likely to be the most common when constructing a `Dockerfile` in an isolated instance. However, there are more commands that can be used and should be used at times. The below are only explained as most of the work necessary to setup a container for a research paper or journal is not that useful. Still, it is recommended to read over the rest of the commands.

### FROM

The `FROM` instruction indicates the base image that this container should be built from. These images are from [Docker Hub](https://hub.docker.com/), which contains images for most implementations. This is generally the first line of your `Dockerfile`.

There exists images for the base operating systems, such as [Debian](https://hub.docker.com/_/debian) or [Ubuntu](https://hub.docker.com/_/ubuntu). There are also more specialized implemenations, such as [Python](https://hub.docker.com/_/python) or [TensorFlow](https://hub.docker.com/r/tensorflow/tensorflow). You can start at any point, you may simply need to do more work within the Dockerfile to get everything you need (e.g., you don't need to install Python using Python or Tensorflow but do for Debian or Ubuntu).

```Dockerfile
# See https://docs.docker.com/reference/dockerfile/#from for more info
FROM <image>:<tag>
```

`<image>` is the image to use and `tag` typically represents the version to use. You can find both of these by searching the required base image on Docker Hub and going to the 'Tags' tab to find whatever version you are looking for.

```Dockerfile
# Installs an image with Debian Bookworm and Python 3.11.9
# No initial slash is needed since Docker maintains this image
FROM python:3.11.9-bookworm

# Installs an image with Ubuntu 22.04 with Python 3.11, TensorFlow 2.16.2, and Jupyter Notebook
# The slash indicates that this repository tensorflow is owned by the tensorflow user
FROM tensorflow/tensorflow:2.16.2-jupyter
```

#### Hardware Emulation

If you want to see the effects of different hardware on individual libraries, you can specify the platform of the image, if the image supports multiple platforms, using the `--platform` argument. This is useful for testing and verifying your code may run on different hardware. This is especially useful since Apple Silicon Macs run a different hardware arhictecutre compared to most Windows and Linux machines.

Most operating systems used are Linux because of their open source nature; however, there are some built for Windows and Mac, though it is unlikely to find them.

**NOTE: To use Hardware Emulation, you need to have Docker Desktop installed or the statically compiled QEMU binaries registered with `binfmt_misc`.**

```Dockerfile
# Installs an image with the AMD64 instruction set (used typically by Windows and Linux machines)
FROM --platform=linux/amd64 python:3.11.9-bookworm

# Installs an image with the ARM64 instruction set (used typically by Apple Silicon Mac machines)
FROM --platform=linux/arm64 python:3.11.9-bookworm
```

### ENV

The `ENV` instruction sets an environment variable in the container. Any set within the `Dockerfile` will persist, while any specified during runtime via `--env <key>=<value>` will only exist for that current run of the container.

```Dockerfile
# See https://docs.docker.com/reference/dockerfile/#env for more info
ENV <key>=<value>
```

`<key>` is the name of the environment variable and `<value>` is the value set for the variable.

```Dockerfile
# 'echo $TEST_VAR' will print "Hello world!"
ENV TEST_VAR="Hello world!"
```

### RUN

The `RUN` instruction will execute any commands on top of the current image. This functionally acts like runnning commands in your terminal. There are additional settings to mount files, manage the network, or handle security as well.

```Dockerfile
# See https://docs.docker.com/reference/dockerfile/#run for more info
RUN <command>

# OR
RUN [ "<command">, ... ]
```

`<command>` is whatever command you want to run.

```Dockerfile
# Create a test directory and write the environment variable to a text file
RUN mkdir /test && echo ${TEST_VAR} > /test/example.txt

# The following is equivalent
RUN [ "mkdir /test", "echo ${TEST_VAR} > /test/example.txt" ]
```

### WORKDIR

The `WORKDIR` instruction indicates the working directory for any instructions that follow it, along with the default entrypoint when opening a terminal within the container. This is effectively like using the `cd` command in a terminal.

```Dockerfile
# See https://docs.docker.com/reference/dockerfile/#workdir for more info
WORKDIR <path>
```

`<path>` is either an absolute or relative value that points to where the running process should go to. If the `path` doesn't exist, it will be created. It is generally recommended to explicitly specify your work directory within the Dockerfile.

```Dockerfile
# Creates the /src directory and starts execution from there
WORKDIR /src
```

## Using a Docker Container

Once a `Dockerfile` is created, it can be used to build the image that the container will use within the isolated and reproducible environment.

### Building the Image

An image can be built using the `build` command. For ease of convenience, it is recommended to use `-t` to specify the image name. The final parameter represents the root directory to build from. That directory must have a `Dockerfile` to define the image.

Say we have the following project:

```
example_project
|-  Dockerfile
|-  docs
|   |-   data.csv
|-  src
    |- analysis.py
```

We can build the image like so, assuming the terminal is within the `example_project` directory:

```bash
# Builds the container from an image definition
# See https://docs.docker.com/reference/cli/docker/image/build/
#     https://docs.docker.com/reference/cli/docker/image/build/#tag
docker build -t <image_name> .
```

`<image_name>` can be replaced with whatever you decide to name the image.

```bash
docker build -t example_image .
```

### Runing the Container

Once the image is built, a container can be built and run using the `run` command. For convenience, it is also useful to specify `-it` along with a `bash` entrypoint like so:

```bash
# Runs the container
# See https://docs.docker.com/reference/cli/docker/container/run/
#     https://docs.docker.com/reference/cli/docker/container/run/#interactive
#     https://docs.docker.com/reference/cli/docker/container/run/#tty
docker run -it <image_name> bash
```

For clarity, `-i` or `--interactive` allows input to the container to be sent through the `STDIN`, meaning you can use the terminal to input data into the container. This, on its own, does not allow writing directly. That is done using the `-t` or `--tty` flag. This attaches a psuedo-TTY to connect your terminal input/output to the container. This effectively functions as if you are writing to the terminal on your current machine.

`<image_name>` represents the name of the image built in the last step to use for the container. Finally, `bash` represents the entrypoint of the container. In this case, we will open up a `bash` prompt in wherever the current working directory is.

> For running the example, you can use `--rm` to immediately delete the container on exit. This goes before the `<image_name>`

```bash
docker run -it example_image bash
```

#### Volumes

Currently, the docker container is isolated, meaning you can't access any of the files on your local machine. To provide access, you can mount a volume to some location within the host. This can be done during runtime by using the `-v` command.

```bash
# See https://docs.docker.com/reference/cli/docker/container/run/#volume
docker run -itv <local_directory>:<remote_directory> <image_name> bash
```

`<local_directory>` refers to the directory on your machine to access within the container. `<remote_directory>` indicates the directory within the container that you can access the local direcctory from. If you want to specify the current working directory in your or the container's terminal, then you can use `${PWD}`.

```bash
# Adds a mount to the current directory to the /src directory in the container
docker run -itv ${PWD}:/src bash
```

### GPU Access

As the container doesn't obtain any access to the host machine, it does not know what hardware you have available. Even if it did understand what hardware was available, you may not be able to leverage the architecture without extensive setup. However, for some pieces of arhictecture, this setup is already provided. For example, using the CUDA toolkit with NVIDIA GPUs can be done by making use of the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit). The toolkit essentially acts as a runtime your container interacts with to provide access to the GPUs.

**NOTE: The toolkit can only be installed on Linux machines. However, most CUDA-accelerated codebases only support Linux anyway.**

To use the toolkit once installed, you need to specify the `--runtime` to be `nvidia` and the `--gpus` you want to access. This can either be the GPU UUID or index, or `all` for all gpus.

```bash
docker run --runtime=nvidia --gpus all -itv ${PWD}:/src example_image bash
```

## Disclaimers

While Docker solves most of the issues with dependencies, it requires a lot of setup to get it to a usable state by the researcher. One example is that docker containers runs as `root` by default and, without any addditional configuration, they would write files to Linux and macOS machines as the root user. Only within the attached volume, but that is still a problem. Getting things working as a non-root user also requires a good number of changes, depending on how much you choose to rewrite. As such, while writing your own container may be very useful, it may not be worth the time and effort needed to do so.
