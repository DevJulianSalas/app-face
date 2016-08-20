# -*- encoding: utf-8 -*-
#Modulo que contiene la configuracion  para la app

#---- build-in Packages----#
from flask import Blueprint

main = Blueprint("appWeb.auth2.0", __name__)

# # Llamamos a todos sus modulos del paquete
from . import controllers, models
