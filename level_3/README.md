# Level 3: Development Containers

TODO

## What are Development Containers?

TODO

## Creating a Devlopment Container

A development container can either be created manually via `.devcontainer/devcontainer.json`, or using a [template]((https://containers.dev/templates)). A template can be used by clicking the `><` blue button in the bottom left corner and selecting `Add Dev Container Configuration Files...`. Then, you just click the options you want, and you're done.

### The Image

The [image](https://containers.dev/implementors/json_reference/) is what's used as a base to create the development container. Images can be found by looking up [devcontainer templates](https://containers.dev/templates); however, it is generally pulling from some container registry like Docker Hub or GitHub. Each image is basically broke into `<url>:<tag>` where the `<url>` points to the image location and `<tag>` indicates what image should be used.

For example, `mcr.microsoft.com/devcontainers/python:1-3.12-bookworm` uses a Python image containing Python 3.12 on Debian Bookworm.

```json5
// In devcontainer.json

// Sets the base image
"image": "mcr.microsoft.com/devcontainers/python:1-3.12-bookworm"
```

If you want to use a `Dockerfile` instead, you can use the `build` block to select the file and the context on where the `Dockerfile` image should use, relative to the `.devcontainer` directory. `build` and `image` are mutually exclusive, meaning you can only have one or the other.

```json5
// In devcontainer.json

// Builds the image from a dockerfile
"build": {
    // Get the name of the Dockerfile
    "dockerfile": "Dockerfile",
    
    // Sets the context location to build the Dockerfile from
    // The Dockerfile must also be in the context location
    "context": ".."
}
```

### Additional Features

[Features](https://containers.dev/implementors/features/) are additional scripts run after the image has been built. These are meant to provide additional tooling to the container without having to write the scripts yourself; however, they are much more powerful. Many images are only built for tags and versions of existing docker containers that had been constructed around its addition somewhere in 2020. However, features are installed via a script, meaning that old versions of software that were not bundled into docker containers can be constructed.

Features are added using the `features` block. Each key represents a feature registry, while every value represents configurations made to the feature. A list of official and community features can be found on the [dev container website](https://containers.dev/features).

```json5
// In devcontainer.json

// Add features to the docker file
"features": {
    // Gets the feature and whatever tagged version
    // "latest" represents the latest version
    // A semantic version can also be used
    // Any missing parts of the semantic version are treated as the latest
    // - 1 will be resolved to 1.6.2
    "ghcr.io/devcontainers/features/python:1": {
        // Configuration info https://github.com/devcontainers/features/tree/main/src/python
        "version": "3.5.10",
        "installTools": false
    }
}
```

### Automation With Post Commands

TODO

### Environment Variables

Development containers have two methods of defining [environment variables](https://containers.dev/implementors/json_reference/): `containerEnv` and `remoteEnv`. Each of these has different use cases depending on what the environment variable is for.

`containerEnv` creates an environment variable within the container itself, meaning that all processes within the container will have access to it. However, these variables are static, meaning the container will need to be rebuilt if the value needs to change.

`remoteEnv` creates an environment variable on the remote using the container only (e.g., the current user). This value can be updated dynamically without having to rebuild the container itself.

Unless you are planning on using environment variables on the local machine or planning to manage different users within the same dev container, it is generally recommended to use `containerEnv`.

```json5
// In devcontainer.json

// Container environment variables
"containerEnv": {
    "CONTAINER_TEST_VAR": "Hello world!"
},


// Remote environment variables
"remoteEnv": {
    "REMOTE_TEST_VAR": "World Hhllo!"
}
```

### Customizations

[Customizations](https://containers.dev/implementors/json_reference/) are simply additional pieces of information associated with the tool loading the development container. For example, Visual Studio Code has a `vscode` block to add additional settings, such as what extensions to load within the container. Customizations are specified via the `customizations` block.

Some customizations come with the images and feautres implemented (e.g., Python extension for Python or R extension for R).

```json5
// In devcontainer.json

// Configure tool-specific properties
"customizations": {
    // Visual Studio Code
    "vscode": {
        // Extensions
        "extensions": [
            // Adds the Jupyter Notebook extension
            "ms-toolsai.jupyter"
        ]
    }
}
```

## Using a Development Container

Once you have created the dev container file in `.devcontainer/devcontainer.json`, using it is relevatively simple. In Visual Studio Code, click the `><` blue button in the bottom left hand corner. A menu should appear in the top middle of your screen. From there, click `Reopen in Container`, and you're done! A new container, or the existing container if it has been initialized before, will be built and Visual Studio Code will automatically remote in as the specified user.

For testing purposes, you may want to rebuild the container from scratch to test whether or not you are making any assumptions. This can be done using `Ctrl (Cmd) + Shift + P` to open up the program menu and selecting `Dev Containers: Rebuild and Reopen in Container` or `Dev Containers: Rebuild without Cache and Reopen in Container` if you want to remove any cached image files and redownload them. 

To see what dev containers are currently available, along with any volumes, you can open up the `Remote Explorer` tab on the sidebar (the computer with the `><` symbol), having the tab on top next to the text selected as `Dev Containers`. You can remove containers and volumes here by right clicking and selecting `Remove Container` or `Remove`, respectively.
