Link: [Sonarqube]
## Setup Instruction
```
poetry install
```

## Run Test
```
poetry run pytest
```

## What to do next

### Install Pre-commit (Recommended)
```
poetry run pre-commit install
```
If you wish to edit pre-commit behavior see ```.pre-commit-config.yaml```.
Normally it checks only the file you are committing. But if you wish to run it manually for all files do
```
poetry run pre-commit run --all
```

### Install Jupyter Notebook Kernel
```
poetry run python -m ipykernel install --user --name python_dummy_project
```

### Adjusting the Dependencies
edit pyproject.toml or just do
```
poetry add numpy
```
or for dev dependencies
```
poetry add --dev numpy
```
See [python-poetry.org](https://python-poetry.org/)

### Change Pytest, Flake, Coverage Setting
See ```tox.ini```

### Change how sonarqube behaves.
See ```sonar-project.properties```

### Get Pycharm to show the correct coverage
Ironically in pycharm test configuration add `--no-cov` to `Additional Arguments` this turn off pytest-cov coverage and uses Pycharm's own pytest.

### Notes:
## Env required:
- PYTHON_VERSION: version of python your project is using
- POETRY_VERSION: version of poetry your project would like to/is using (check compatibility before specify)
- PROJECT_KEY: directory of your project, format: <(username/organisation)>_<repository_name>
- AZURE_WEBAPP_NAME: the name of your project in Azure, should set to match the created Web App in Azure's App Service

## Secrets required:
- SONAR_TOKEN: Credential token for sonarcloud's functionality. Acquired from Sonarcloud's website '''https://sonarcloud.io/'''. Get it from My Account -> Security -> Then generate a new token for this
- AZUREAPPSERVICE_PUBLISHPROFILE_<random 32 bit of hexs>: Location token for Azure deployment endpoint. Acquired from Microsoft Azure's App Service -> Web App -> Deployment Center -> Look for this in the auto generated workflow

 
 
