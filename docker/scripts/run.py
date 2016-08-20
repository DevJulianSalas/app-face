#! /usr/bin/env python

# --- build-in Packages ---
import os

# --- Own Packages ---
from appWeb import create_app
# from app.auxiliary_functions import object_celery as cf



# Creamos la app para correrla
app = create_app(os.getenv("FLASK_CONFIG") or "default")
# celery = cf.make_celery(app)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
