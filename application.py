# -*- coding: utf-8 -*-
from flask import Flask, render_template
from operator import itemgetter
from utils import yaml

application = Flask("application")

@application.route("/")
def hello():
    classmates = yaml.loadfile('sample_data.yml')
    return render_template("table.html", persons=sorted(classmates, key=itemgetter('name')))
     

if __name__ == "__main__":

    application.run()