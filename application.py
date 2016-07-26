# -*- coding: utf-8 -*-
import os 
import json
from flask import Flask, render_template
from operator import itemgetter


application = Flask("application")
MAIN_PAGE_TEMPLATE_FILE = "table.html"
CLASSMATES_JSON_PATH = os.path.join('classmates.json')


def get_classmates():
    with open(CLASSMATES_JSON_PATH, 'r') as file:
        return json.load(file)
        
@application.route("/")
def hello():      
    classmates = sorted(get_classmates(),key=itemgetter('group'))
    return render_template(MAIN_PAGE_TEMPLATE_FILE, persons=classmates)


if __name__ == "__main__":
    print(sorted(get_classmates(),key=itemgetter('group', 'name')))
    application.run(debug = True)
    