# cookiecutter-science
The  template to start a new science project in Vizzuality.

## Setup a new project
First you need to have `cookiecutter` installed in your system. 
You can find some guidance in the [installation docs](https://cookiecutter.readthedocs.io/en/2.0.2/installation.html). 
I recomend going the [pipx](https://pypa.github.io/pipx/) way to deal with this kind of global do-the-same-one-thing programs. 

Then you can run the following command to create a new project from a local copy of the template:
```bash
cookiecutter path/to/cookiecutter-science
```
or use directly the github repo as a source for the template:

```bash
cookiecutter https://github.com/vizzTools/cookiecutter-science
```

## What's in the box?
The template will create a new project with the following structure:

```
├── README.md                   # the landing page for your project
│                                   Must contain all the importat information about the project.
├── data
│   ├── raw                     # a place for raw data.
│   └── processed               # a place for processed data.   
│  
├── notebooks                   # a place for jupyter notebooks (only "final" versions please).
│  
├── src                         # a place for python scripts.
│   └── __init__.py
│  
├── environment.yml             # conda/mamba environment file.
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml              # python project file for global configuration.
├── LICENCE
├── .pre-commit-config.yaml     # pre-commit hooks configuration.
├── .gitignore
├── .editorconfig               # how many spaces and indentation your ide has to use.
└── .env.example                # example of .env file.
```
Simple.

### Conda environment
The template comes with a `conda` environment file. But we will use `mamba` 
to create and manage the environment. The environment has a basic set of packages that more or less 
are the common ground of our projects. You can find the list of packages in the `environment.yml` file.

Once the project you will have the instructions on how to create and update the environment in the `README.md` file.

### Docker
The template comes with a `Dockerfile` and a `docker-compose.yml` file. This allows to run the project notebooks 
in a fully isolated environment in case the local installation of the environment fails, 
or if it is more of your preference.

The `docker-compose.yml` file is configured to mount the project folder and spin up 
a jupyter server.

### Pre-commit hooks and code formatting
The template comes with a set of pre-commit hooks configured in the `.pre-commit-config.yaml` file.

This is quite important since it will help you to keep your code clean and tidy. so 
**please always install the hooks** when you start a new project.

```shell
pre-commit install
```

To format the code so that the hooks don't complain you **must** 
use the `black` formatter and `isort` to sort the imports.

The jupyter lab in the env has an installed extension to format the notebooks:

![format-notebook.png](imgs/format-notebook.png)

If you work in vscode you can install the black formatter and the isort extension to format the code on save. 
Same for pycharm.

Also, the environment has the `nbqa` package installed. This allows you to run the formatters and linters 
to the notebooks from the command line. For example:

```shell
nbqa black notebooks/
```

will format all the notebooks in the `notebooks/` folder.

```shell
nbqa isort notebooks/
```

will sort the imports in all the notebooks in the `notebooks/` folder. And finally
    
```shell
nbqa ruff notebooks/
```

will highlight the cells that have code and style issues in them.