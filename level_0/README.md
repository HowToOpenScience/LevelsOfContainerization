# Level 0: The Bare Minimum

Level 0 refers to the bare minimum all projects should have when attempting use materials, regardless of sharing. There are four main concepts: making sure your materials run, documenting the materials, recording dependency versions, and a README explaining how to use the materials.

## Make Sure Your Materials Run!!!!

First, you should make sure your materials are able to run when executed. This may seem trivial, but across the ~30 papers tested within education technology in 2022 and 2021, at approximately 1/3 of the papers did not run after setting up the exact same or similar environments. Most of the code had to be rewritten in some capacity to reproduce the results reported.

The easiest way to verify your code runs is by using one of the subsequent levels. However, another method is to have another labmate run your codebase on their machine to test whether or not it works. Most machines have setups from previous projects that makes the researcher assume that all materials are provided. By having another run your materials, you can guarantee that there are no underlying assumptions on your machine that may make reproduction impossible.

The following are a list of recommendations to make it more likely that your materials will run on another machine.

### Use Relative File Paths

The only thing you can typically guarantee about your materials is the organization of the project folder. However, where that project folder is located may differ across machines. On Windows, this may be in `C:\Users\<username>\Documents\Projects\<project_folder>`. On Linux, it could be in `/home/<username>/<project_folder>`. On a different Windows machine, it may be in `C:\Users\<username>\Projects\<project_folder>`. You cannot say for certain whether files will be in the same location. As such, all file operations should take place only within the project folder and using relative paths.

Say we had the following project file structure within `/home/example_user/example_project`:

```
root
|-  docs
|   |-   data.csv
|-  analysis.py
```

```bash
example_user:~/example_project$ python analysis.py
```

We could read the file like so from `analysis.py`:

```python
with open('./docs/data.csv') as file:
    # Do stuff here
```

Relative paths resolve dynamically. A `.` represents the current directory of where the executable is running (which is usually the location the file is within). A `..` represents the parent directory of where the executable is running.

If we have a different file structure:

```
example_project
|-  docs
|   |-   data.csv
|-  src
    |- analysis.py
```

The following python code would remain the same if we ran the code from the `example_project` directory:

```bash
example_user:~/example_project$ python src/analysis.py
```

```python
# In analysis.py
with open('./docs/data.csv') as file:
    # Do stuff here
```

However, it would change if we ran it from the directory `analysis.py` was in:


```bash
example_user:~/example_project/src$ python analysis.py
```

```python
# In analysis.py
with open('../docs/data.csv') as file:
    # Do stuff here
```

The `..` brings us back to the `example_project` directory.

So make sure that everything is running in the correct context!

### Avoid OS Specific Implementations

Take a look at the following commands to rename files. This is used to strip timestamps (e.g. `testfile_2024_07_01.txt` will be renamed to `testfile.txt`).

```bash
# Linux
sed 's/([A-Za-z_]\+)_[0-9_]\+\.txt/\1\.txt/'

# macOS
sed -E 's/([A-Za-z_]+)_[0-9_]+\.txt/\1\.txt/'

# Windows PowerShell
Get-ChildItem *.txt | Rename-Item -NewName { $_.Name -replace '([A-Za-z_]+)_[0-9_]+\.txt)', '$1\.txt'}

```

Each command is different with potentially differing file extensions, meaning that the files themselves will likely fail across different machines. Therefore, it is generally not recommended to use OS specific implementations to perform operations. Instead, use high level programming languages as they perform these conversions behind the scene.

```python
# In some python file
# Borrowed from https://stackoverflow.com/a/55856360

from glob import glob
import os
import re
import sys

# Gets the regex to check file name
renamer = re.compile(r"([A-Za-z_]+)_[0-9_]+\.txt", flags=re.I).sub

# Get the current directory
working_directory = sys.argv[1]

# Loop through files in directory
for old_path in glob(os.path.join(work_dir, '*.txt')):
    dirname, old_name = os.path.split(old_path)
    # Get rename
    new_name = renamer('\\1.txt', old_name)
    new_path = os.path.join(dirname, new_name)

    # Rename file
    os.rename(old_path, new_path)

```

This will work regardless of what machine you are working on.

### Check Any Downloaded Materials

There are many pieces of software that downloads models or dataset for you to use on your machine. Most researchers tend to run the command themselves in some terminal to choose what datasets to download. However, as this step isn't normally recorded, running the materials on a different computer can result in an error that may not always be descriptive enough to figure out what's going on. In these scenarios, you should either include the download step within the materials itself or have it written down in some location.

The most common occurence of this comes when using huggingface or nltk:

```bash
# For nltk, include this command somwhere
python -m nltk.downloader <package_id>
```

```python
# In python
import nltk

nltk.download('<package_id>')
```

## Document Materials

Documentation is generally necessary to not only understand, but remember what your code is doing. You do not need to document every single thing, but you should generally provide enough information that the codebase is understandable at a glance.

See the example within [`01_docs`](./01_docs/). To setup:

```bash
# Navigate to the directory
cd 01_docs

# Setup the virtual environment
python -m venv docs_env

# Activate the environment (bash/zsh)
# See https://docs.python.org/3/library/venv.html#how-venvs-work for more info
source ./docs_env/bin/activate # or './docs_env/Scripts/activate' on Windows

# Install requirements
python -m pip install -r docs_env_requirements.txt

# Look at script code
```

## Record Dependencies and Versions

The dependencies, along with their versions, your materials rely on should be recorded in some location. Otherwise, it is highly likely the codebase will not run. This disparity will get worse over time as the as newer libraries may be supported as dependencies of things you depend on, which may prevent the project from being recoverable without massive quantities of work. Some papers reviewed from previous years encountered this issue, taking over 40 hours of work to get the dependencies to a workable state.

There are methods to record the dependencies of your work usually built into the language or package manager you are using. You should also record the version of the language, as that may not be supports in the language or package manager in question.

```bash
# For Python 3.12.4, write the requirements to a text file
pythom -m pip freeze > requirements.txt
```

### Semantic Versioning

Versioning is usually broken down into three numbers separate by dots (e.g., `1.12.4`). This is known as [semantic versioning](https://semver.org/), and the differences between these numbers usually indicates whether or not your codebase will work with a version different from your own.

The number is broken down into `<major>.<minor>.<patch>`.

`patch` is incremented if backwards compatible bug fixes are introduced. This means that `1.12.3` and `1.12.40` will likely work on the same materials. This won't be the case if the method you are using relies on experimental sections of the codebase that do not follow the versioning scheme, or if the method you are using has incorrect behavior that was fixed as part of a patch.

`minor` is incremented if backwards compatible functionality is added, for example a new fuction. This means that functions within `1.12.0` will still exist within `1.13.0`. However, using a function from `1.13.0` will not exist in `1.12.0`.

`major` is incremented if backwards imcompatible functionality is added, such as modifying existing functions or removing them completely. There is no guarantee that a codebase written in `1.0.0` will work in `2.0.0`, or vice versa.

Generally, it is best to assume that only versions that differ by patch will work across different machines. Many materials still remove functionality in `minor` versions, leaving complete rewrites for `major` versions. Programming languages like Python and R take this approach. 

See the example within [`00_dependencies`](./00_dependencies/). To setup:

```bash
# Navigate to the directory
cd 00_dependencies

# Setup the virtual environments
python -m venv env_old
python -m venv env_new

# Activate environment (bash/zsh)
# See https://docs.python.org/3/library/venv.html#how-venvs-work for more info
source ./env_old/bin/activate # or './docs_env/Scripts/activate' on Windows

# Install requirements
python -m pip install -r env_old_requirements.txt

# Run script
python main.py

# Repeat for second environment
deactivate
source ./env_new/bin/activate
python -m pip install -r env_new_requirements.txt
python main.py
```

## Write a README

READMEs are useful for explaining what the project is. READMEs can either contain or contain links to documentation about the project, how to use the materials, how to setup and contribute to the project, citation information, additional resources, etc. It is generally recommended to have one such that if you or anyone else sees your project, they can understand the broad strokes and get started with using the materials.
