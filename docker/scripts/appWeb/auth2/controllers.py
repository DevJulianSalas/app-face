# -*- coding: utf-8 -*-

# -- Packages Build-in --
# -- Packages Installed --
from flask import Flask
# -- Own Packages --
from . import main

@main.route("/index")
def index():
    return "index"
