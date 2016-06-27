# -*- coding: utf-8 -*-
from flask import Flask, render_template
from operator import itemgetter
from yaml_import import CLASSMATES

application = Flask("application")


@application.route("/")
def hello():
    return render_template("table.html", persons=sorted(CLASSMATES, key=itemgetter('name')))
     

if __name__ == "__main__":
    application.run()
