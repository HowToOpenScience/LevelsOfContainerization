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
pyhton -m pip install scikit-learn==1.5.0

# Check downloaded version
python -m pip show scikit-learn # or pip freeze if version too old
```

Once you are done with the local environment, you can run the `deactivate` command to return to the global environment.

```bash
source deactivate # or 'deactivate' on Windows
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

TODO

- poetry (curl -sSL https://install.python-poetry.org | python3 -)
    - poetry completions bash >> ~/.bash_completion

### Setting up a Build Tool

TODO

### Using a Build Tool

TODO

## Disclaimers

While this may handle dependency management for you, thus reducing the burden somewhat, this still has many of the same issues has Level 0. Everything is still being done locally, which while not usually an issue, could cause some amount of headache depending on the machine.
