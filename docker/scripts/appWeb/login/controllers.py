# -*- coding: utf-8 -*-

# -- Packages Build-in --
# -- Packages Installed --
from flask import render_template, url_for
# -- Own Packages --
from . import login

@login.route("/index")
def index():
    return render_template("login.html")
