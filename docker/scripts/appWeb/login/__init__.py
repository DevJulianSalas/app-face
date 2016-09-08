# -*- encoding: utf-8 -*-
#Modulo que contiene la configuracion  para la app

#---- build-in Packages----#
from flask import Blueprint

main = Blueprint("login",  __name__,
                 template_folder="templates",
                 static_folder="static"
)

# # Llamamos a todos sus modulos del paquete
from . import controllers, models
