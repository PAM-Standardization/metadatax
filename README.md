# metadatax

metadatax is a Django app.


### Quick start


1. Add "metadatax" to your INSTALLED_APPS setting like this::
```python
    INSTALLED_APPS = [
        ...,
        "metadatax",
    ]
```
2. Include the metadatax URLconf in your project urls.py like this::
```python
    path("metadatax/", include("metadatax.urls")),
```
3. Run `python manage.py migrate` to create the models.

4. Visit the `/metadatax/` URL to access the metadatax.