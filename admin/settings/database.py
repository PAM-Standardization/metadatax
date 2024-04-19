"""
Database config
"""


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "metadatax",
        "USER": "",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "PORT": 5432,
    }
}
# You should run docker run -e POSTGRES_PASSWORD=postgres -p 127.0.0.1:5433:5432 -d postgis/postgis
