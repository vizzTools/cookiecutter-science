{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

--------

## Setup

### First, the environment

#### Docker

With [docker]() in your system, you can develop inside containers:

``` bash
docker compose up --build
```

And if you want to get into the container, use a terminal in jupyter lab, vscode or jump in the running
container with:

```shell
docker exec -it {{ cookiecutter.project_slug }}_notebooks /bin/bash
```

#### Locally

To use a 100% reproducible env use always [conda-lock](https://github.com/conda/conda-lock#installation)
With conda lock in your system, you can create the environment with:

``` bash
mamba env create -n {{cookiecutter.project_name}} -f environment.yml
```
This will create and environment called {{cookiecutter.project_name}} with a common set of dependencies.

### Second, initialize git (if needed) and the pre-commit hooks

If this is a new, standalone project, you need to initialize git:

``` bash
git init
```

If the project is already in a git repository (or a module in a bigger project), you can skip this step.

To install the code checks, in the environment and in this directory, run:

``` bash
pre-commit install
```

## Update the environment

If you need to update the environment installing a new package, you simply do it with:

``` bash
mamba install [package]
```

or 

```bash
pip install [package]
```
then update the environment.yml file so others can clone your environment with:

``` bash
mamba env export --no-builds -f environment.yml
```
