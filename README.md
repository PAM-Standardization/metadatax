# metadatax

metadatax is a Django app.


## Overview
Here is a schema of the database structure
![v2 - Métadonnées d'acquisition](./schema.svg)


## Quick start
### Local development
In your `pyproject.toml` add 
```toml
metadatax = { path = "path/to/metadatax/root", develop = true }
```
This will give full access to metadatax in your project and it will see every changes on you local metadatax project.

##### Before commit
Run black to format your code:
```shell
poetry run black admin meta_auth metadatax website
```

### In your project
1. Add "metadatax" to your INSTALLED_APPS setting like this::
```python
    INSTALLED_APPS = [
        ...,
        "django_admin_multiple_choice_list_filter",
        'django_better_admin_arrayfield',
        "graphene_django_optimizer",
        "metadatax",
        "metadatax.common",
        "metadatax.bibliography",
        "metadatax.ontology",
        "metadatax.acquisition",
        "metadatax.equipment",
        "metadatax.data",
    ]
```
2. Include the metadatax URLconf in your project urls.py like this::
```python
  path("metadatax/", include("metadatax.urls")),
```
3. Run `python manage.py migrate` to create the models.

4. Visit the `/metadatax/` URL to access the metadatax.


## Deployment
### Environment
Create a `.env` file at the root of the project with the following content:
```.env
DEBUG=TRUE
SECRET_KEY=

HOST=                           ## Needed only if DEBUG=False
STATIC_ROOT=                    ## Needed only if DEBUG=False

DB_USERNAME=
DB_PASSWORD=
DB_PORT=                        ## Default used is 5432
```
