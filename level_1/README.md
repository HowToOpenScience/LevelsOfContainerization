# Level 1: Local Environments and Build Tools

Level 1 contains the next step up when using materials: local environments to isolate your dependencies, and build tools to help automate the setup process. For non-OS related requirements, this is generally what most researchers should do to share exactly what's needed.

## What are Local Environments?

Local environments are a separate location from your global installation to install pacakges for use with your project. You can think of them as project libraries, where each project has its own library of packages to use. They can generally not access other packages from the global installation without configuration.

An extension upon this is virtual environments. Compared to local environments, the individual compiler and interpreter are isolated as well. This makes for a completely unique instance of the language and package separated from the global implementaiton.

Local environments are useful for separating the dependency requirements needed for each project. In a single global environment, you can only have one version of each package. However, each local environment can have a different version, allowing you to use other materials without having to ruin your own environment. Additionally, it also helps with separating what is used by the project and what isn't. A global environment will include packages the researcher does not need to run the project, so a local environment can only install the necessary details.

### Setting Up a Local Environment

Python uses the stricter [virtual environment](https://docs.python.org/3/library/venv.html); however, we will continue to call them virtual environments. You may have already seen these environments in Level 0 when going over the examples.

Python local environments are created using the `venv` module. All that is needed is the directory where the environment will be generated.

```bash
# Setup the virtual environment
# <directory> is the location of the virtual environment
python -m venv <directory>
```

```bash
python -m venv example_venv
```

### Using a Local Environment

To use the local environment, you need to call the `activate` script located within `<directory>/bin` for POSIX machines (e.g., Linux, macOS) or `<directory>/Scripts` for Windows machines.

```bash
# Activate environment (bash/zsh)
# See https://docs.python.org/3/library/venv.html#how-venvs-work for more info
source ./example_venv/bin/activate # or './example_venv/Scripts/activate' on Windows
```

Within your terminal, you should notice a difference, specifically the name of the environment prepended onto the terminal text:

```bash
# Before
example_user@example_machine:~/example_project$ 

# After running activate
(<directory>) example_user@example_machine:~/example_project$ 
```

This indicates that you are within the Python local environment. When you run any Python commands, it use the environment context rather than the global context.

```bash
# Download package
python -m pip install scikit-learn==1.5.0

# Check downloaded version
python -m pip show scikit-learn # or pip freeze if version too old
```

Once you are done with the local environment, you can run the `deactivate` command to return to the global environment.

```bash
deactivate # or 'source deactivate' depending on context
```

You will be able to see the difference once again with the environment removed.

```bash
# Before
(<directory>) example_user@example_machine:~/example_project$ 

# After running deactivate
example_user@example_machine:~/example_project$ 
```

You can also check the currently installed libraries to see that you only have access to the versions in your global environment.

```bash
# Check downloaded version
python -m pip show scikit-learn # or pip freeze if version too old
```

### Exporting Dependencies

To export the dependencies of your Python local environment, you can run the `pip freeze` command and pipe the output to a text file. Most tend to call it `requirements.txt`. This is typically sufficient for reproducibility as long as the Python version is mentioned in a README.

```bash
# Make sure you are in the local environment
# If not, activate the environment
# See https://docs.python.org/3/library/venv.html#how-venvs-work for more info
source ./example_venv/bin/activate # or './example_venv/Scripts/activate' on Windows

# Output requirements to a text file
python -m pip freeze > requirements.txt
```

If you want to use these requirements later on, you can use the `-r` to specify the file of what dependencies to download.

```bash
# Download dependencies
python -m pip install -r requirements.txt
```

## What are Build Tools?

Build tools are meant as a method to handle how a program should compile, run, and build. This typically includes dependency management, which is the main purpose we should use a build tool in research. This automates and simplifies some of the processes of using a local environment; however, if you are not planning on doing anything complicated within the project, either solution will work fine.

For this example, we will use [Poetry](https://pypi.org/project/poetry-core/) as the build tool, but there are plenty of others that may be more suited for whatever project you are using. You could also choose not to use a build tool as well since their general benefit is a simplified setup without needing to track dependencies outside of when you specify them for installation.

### Setting up a Build Tool

Poetry does not require much setup, only needing three blocks within a `pyproject.toml` file: the main `poetry` block, the `build-system` block, and the `dependencies` block.

The `poetry` and `build-system` block are basically copy-paste from any project. The `poetry` block (or `tool.poetry`) simply contains a reference to [`package-mode`](https://python-poetry.org/docs/basic-usage/#operating-modes) to set the value to false. This tells our project to only use it for dependency management and not for building a release to put on some Python library repository. The [`build-system` block](https://python-poetry.org/docs/pyproject/#poetry-and-pep-517) is meant as a compliance factor to `PEP-517` to indicate Poetry is used to build this project.

```toml
# Poetry block
[tool.poetry]
package-mode = false

# Build system block
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

The `dependencies` block (or `tool.poetry.dependencies`) contains the dependencies that this project will use. It is recommended to add dependencies via `poetry add` to avoid having to learn the syntax yourself. You will need to add a manual version for `python` though: `^3.x` where `x` is the minor version of Python you are using.

```bash
# Add a library to the poetry project
## It will ask you to specify a version. None specified means latest
poetry add pandas
```

```toml
# Dependencies block
[tool.poetry.dependencies]
# Any Python version from 3.12.0 inclusive to 3.13.0 exclusive
python = "~3.12"
# Any pandas version from 2.2.2 inclusive to 3.0.0 exclusive
pandas = "^2.2.2"
```

### Using a Build Tool

Poetry can be used similar to a local environment but with the commands changed around:

```bash
# Creates the local environment
poetry shell

# Installs any dependencies from the Poetry package in the local environment
poetry install

# Leave the local environment
## One of the following
exit
deactivate # or 'source deactivate' in certain contexts

# If you need to reenter the local environment if it hasn't been cleaned up:
source $(poetry env info --path)/bin/activate # or '& ((poetry env info --path) + "\Scripts\activate.ps1")' on Windows
```

## Disclaimers

While this may handle dependency management for you, thus reducing the burden somewhat, this still has many of the same issues has Level 0. Everything is still being done locally, which while not usually an issue, could cause some amount of headache depending on the machine.
