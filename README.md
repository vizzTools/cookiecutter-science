# cookiecutter-science

The template to start a new science project in Vizzuality.

## Setup a new project

First you need to have `cookiecutter` installed in your system.
Follow the instructions in the [installation docs](https://cookiecutter.readthedocs.io/en/2.0.2/installation.html).
I recommend going with the [pipx](https://pypa.github.io/pipx/) way
to deal with this kind programs.

With cookiecutter installed, run the following command to create a new project from a local copy of the template:

```bash
cookiecutter path/to/cookiecutter-science
```

or use directly the GitHub repo as a source for the template:

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
│   └── _template.ipynb          # a template notebook with some useful structure.
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
└── .env                        # example of .env file.
```

Simple.

### Conda environment

The template comes with a `conda` environment file.
I strongly recommend the use of [`mamba`](https://mamba.readthedocs.io/en/latest/)
to create and manage the environment. The environment has a basic set of packages that more or less
are the common ground of our projects. You can find the list of packages in the `environment.yml` file.

Probably you will need to add more packages to your environment according to your/project needs.
Once the project is created, you will have the instructions on how to create and update the environment in
the `README.md` file.

### Docker

The template comes with a `Dockerfile` and a `docker-compose.yml` file.
It allows running the project notebooks in a fully isolated environment.

The `docker-compose.yml` file is configured to mount the project folder and spin up
a jupyter server.

### Pre-commit hooks and code formatting

The template has a set of pre-commit hooks configured in the `.pre-commit-config.yaml` file.
It is a crucial part of the template. The hooks will run every time you commit changes to the repo.
This way we can ensure that the code is formatted and standardized according to the best practices.

To install pre-commit, there are multiple options:

- Installing the environment provided in the template locally, since it has pre-commit installed.
- Installing pre-commit in your system as globally available package or using [pipx](https://pypa.github.io/pipx/).

when you start a new project run the following command in the root of the project:

```shell
pre-commit install
```

⚠ **Please always run this** at the start of a new project.

This will autoformat the code and run the linters every time you commit changes to the repo.

To format the code manually, it is a **must** to use [`ruff format`](https://docs.astral.sh/ruff/formatter/).

#### Notebooks

In Jupyter Lab, the env has an installed extension to format the notebooks:

![format-notebook.png](imgs/format-notebook.png)

#### Ruff

To format and lint notebooks and python files, the environment has the
[`ruff`](https://nbqa.readthedocs.io/en/latest/index.html) package installed and configured to inspect .ipynb too.
This allows you to run the formatters and linters for notebooks from the command line.
For example:

```shell
ruff format .
```

will format everything in the project folder (including notebooks).

```shell
ruff check --fix .
```

will lint (and fix inplace the fixable issues) all the files in the project.

## Notebook style guide and general guidelines

The template comes with a template notebook in the `notebooks/` folder called `_template.ipynb`. It has a simple
structure as a starting point for your notebooks.
Remember that the notebooks **are a way to communicate your work**, so it is important to keep them clean and tidy.
Here are some musts and guidelines to follow:

⛔ Never include secrets or sensitive information in the git tracked files. If you need to use secrets, use the `.env`.

🤯 Keep only the outputs of the cells that are important for understanding the process (plots, result values, etc.).
**Avoid** any sort of **long output** that will clutter the revision of the notebook or make it difficult to read
(whole dataframes, debug messages, gdal command outputs, etc.). Don't upload empty cells.

🏁 Always try to **make your notebooks idempotent**.
This means that you can run the cells any number of times and the result is always the same.

💀 Avoid leaving superfluous or dead code. If you don't use it, delete it.

🗄 Don't upload data files. Use a bucket in the cloud and load the data from there.

🏞 Use markdown cells to explain what you are doing and why.

📇 Group code and explanations in sections of related topics.

🗂 Make a section of util functions or a separate file of utils
and import it with `%run analysis_utils.ipynb` if needed. This way you can keep the notebook clean.

📜 Make a script in `src/` instead of a notebook if the process will be part of a data pipeline,
run in a server or simply if you think that it will be cleaner.

If you need some inspiration, take a look at
the [Peter Norvig's pytudes notebooks](https://github.com/norvig/pytudes/tree/main/ipynb).
They are a great example of how to use notebooks in a clean and tidy way. For
example [this one](https://github.com/norvig/pytudes/blob/main/ipynb/Economics.ipynb).
