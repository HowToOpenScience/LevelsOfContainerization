# Level 2 : Docker Containers

TODO

## What is a Docker Container?

TODO

## Setting up a Docker Container (the Dockerfile)

TODO

- Making a docker container
- FROM, ARG, ENV, RUN

### FROM

The `FROM` instruction indicates the base image that this container should be built from. These images are from [Docker Hub](https://hub.docker.com/), which contains images for most implementations. This is generally the first line of your `Dockerfile`.

There exists images for the base operating systems, such as [Debian](https://hub.docker.com/_/debian) or [Ubuntu](https://hub.docker.com/_/ubuntu). There are also more specialized implemenations, such as [Python](https://hub.docker.com/_/python) or [TensorFlow](https://hub.docker.com/r/tensorflow/tensorflow). You can start at any point, you may simply need to do more work within the Dockerfile to get everything you need (e.g., you don't need to install Python using Python or Tensorflow but do for Debian or Ubuntu).

`FROM` is formatted like so:

```Dockerfile
FROM <image>:<tag>
```

Where `<image>` is the image to use and `tag` typically represents the version to use. You can find both of these by searching the required base image on Docker Hub and going to the 'Tags' tab to find whatever version you are looking for.

```Dockerfile
# See https://docs.docker.com/reference/dockerfile/#from for more info

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

### ARG and ENV

TODO

### RUN

TODO

### WORKDIR

TODO

## Using a Docker Container

TODO

### Building the Container

TODO

### Runing the Container

TODO

#### Volumes

TODO

- Volumes

### GPU Access

TODO

- GPU Access for nvidia
