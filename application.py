# -*- coding: utf-8 -*-

import json
from flask import Flask, render_template
from operator import itemgetter


application = Flask("application")
MAIN_PAGE_TEMPLATE_FILE = "table.html"
CLASSMATES_JSON_PATH = 'classmates.json'


def get_classmates():
    with open(CLASSMATES_JSON_PATH, 'r') as file:
        return json.load(file)
      
CLASS_PEOPLE = sorted(get_classmates(),key=itemgetter('group', 'name'))
      
@application.route("/")
def hello():      
    return render_template(MAIN_PAGE_TEMPLATE_FILE, persons=CLASS_PEOPLE)


if __name__ == "__main__":
    print(CLASS_PEOPLE)
    application.run(debug = True)
    