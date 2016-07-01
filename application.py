# -*- coding: utf-8 -*-
from flask import Flask, render_template
from operator import itemgetter

from userdata.from_xl import get_printable  

application = Flask("application")
MAIN_PAGE_TEMPLATE_FILE = "table.html"

def get_classmates():
    return [{'name':x[0], 'url':"https://www.facebook.com/" + x[1]} for x in get_printable()]
    
@application.route("/")
def hello():
    classmates = get_classmates()
    return render_template(MAIN_PAGE_TEMPLATE_FILE, persons=sorted(classmates, key=itemgetter('name')))

if __name__ == "__main__":
    print(get_classmates())
    application.run(debug = True)