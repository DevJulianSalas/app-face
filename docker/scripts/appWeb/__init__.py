# -*- encoding: utf-8 -*-
#Modulo que contiene la app de flask de acuerdo al contexto development, production or testing


#---- build-in Packages ----#


# --- Installed Packages ---#
from flask import Flask
from flask.ext.bootstrap import Bootstrap
#---- Own Packages ----#
from config import config


def create_app(config_name):
    """Crea la app flask de acuerdo al contexto."""
    app  = Flask(__name__)
    app.config.from_object(config[config_name])
    # bootstrap = Bootstrap(app)
    # print bootstrap

    # 1 blueprint para app send_data
    from appWeb.login import login as login_blueprint
    from appWeb.dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(login_blueprint)
    app.register_blueprint(dashboard_blueprint)
    return app
