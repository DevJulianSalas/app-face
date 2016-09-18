# -*- coding: utf-8 -*-

# -- Packages Build-in --
# -- Packages Installed --
from flask import render_template, url_for
# -- Own Packages --
from . import dashboard


@dashboard.route("/dashboard")
def index():
    return render_template("dashboard.html")
