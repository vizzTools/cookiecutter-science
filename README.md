# cookiecutter-science
The template to start a new science project in Vizzuality.

## Setup a new project
First you need to have `cookiecutter` installed in your system. 
Follow the instructions in the [installation docs](https://cookiecutter.readthedocs.io/en/2.0.2/installation.html). 
I recommend going with the [pipx](https://pypa.github.io/pipx/) way
to deal with this kind programs. 

With cookiecutter installed, run the following command to create a new project from a local copy of the template:
```bash
$ cookiecutter path/to/cookiecutter-science
```
or use directly the GitHub repo as a source for the template:

```bash
$ cookiecutter https://github.com/vizzTools/cookiecutter-science
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
The template comes with a `conda` environment file. 
I strongly recommend the use  of [`mamba`](https://mamba.readthedocs.io/en/latest/) 
to create and manage the environment. The environment has a basic set of packages that more or less 
are the common ground of our projects. You can find the list of packages in the `environment.yml` file. 

Probably you will need to add more packages to your environment according to your/project needs.
Once the project is created, you will have the instructions on how to create and update the environment in the `README.md` file.

### Docker
The template comes with a `Dockerfile` and a `docker-compose.yml` file. 
It allows running the project notebooks in a fully isolated environment.

The `docker-compose.yml` file is configured to mount the project folder and spin up 
a jupyter server.

### Pre-commit hooks and code formatting
The template has a set of pre-commit hooks configured in the `.pre-commit-config.yaml` file.
It is a crucial part of the template. The hooks will run every time you commit changes to the repo. 
This way we can ensure that the code is formatted and standardized according to the best practices.
**Please always install the hooks** when you start a new project with:

```shell
$ pre-commit install
```

To format the code so that the hooks don't complain you **must** 
use the `black` formatter and `isort` to sort the imports.

#### Notebooks
The jupyter lab in the env has an installed extension to format the notebooks:

![format-notebook.png](imgs/format-notebook.png)

#### nbqa

Also, the environment has the [`nbqa`](https://nbqa.readthedocs.io/en/latest/index.html) package installed. 
This allows you to run the formatters and linters to the notebooks from the command line. For example:

```shell
$ nbqa black notebooks/
```

will format all the notebooks in the `notebooks/` folder.

```shell
$ nbqa isort notebooks/
```

will sort the imports in all the notebooks in the `notebooks/` folder. 

Finally, to lint the code in cells with `ruff`:
    
```shell
$ nbqa ruff notebooks/
```

#### Scripts and IDEs
If you work in Vscode, you can install the black formatter and the isort extension to format the code on save. 
Same for pycharm. 
If you don't use any of these IDEs, you can always run the formatters from the command line (inside the env):

```shell
$ black src/
```

```shell
$ isort src/
```

_Note: the notebook engine in Vscode and pycharm is a bit more fiddly to configure for formatting and linting. 
Use the black and isort extensions available in the marketplace and check for notebook support._
