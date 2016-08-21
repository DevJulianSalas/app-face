# -*- coding: utf-8 -*-

# -- Packages Build-in --
# -- Packages Installed --
from flask import render_template
# -- Own Packages --
from . import main

@main.route("/index")
def index():
    return render_template()
