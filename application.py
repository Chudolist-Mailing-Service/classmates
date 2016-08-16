# -*- coding: utf-8 -*-

import json
from transliterate import translit
from flask import Flask, render_template
from operator import itemgetter

application = Flask("application")
MAIN_PAGE_TEMPLATE = "table.html"
GROUP_PAGE_TEMPLATE = "group.html"

CLASSMATES_JSON_PATH = 'classmates.json'

def get_classmates():
    
    #load json
    with open(CLASSMATES_JSON_PATH, 'r') as file:
        people = json.load(file)
    
    #add verson of translit name 
    for p in people:
        p['translit'] = translit(p['name'], 'ru', reversed=True).replace(" ", "_").replace("'","") + "_" + p['group']
    
    # order list by proup and name
    return sorted(people,key=itemgetter('group', 'name'))
      
CLASS99_PEOPLE = get_classmates()
TRANSLIT_NAMES = [p['translit'] for p in get_classmates()]

def get_group_list(group_n):
    return [p for p in CLASS99_PEOPLE if p['group'] == str(group_n)]
        
@application.route("/")
def hello():      
    return render_template(MAIN_PAGE_TEMPLATE_FILE, persons=CLASS99_PEOPLE)

@application.route('/user/<username>')
def show_user_profile(username):
    if username in TRANSLIT_NAMES:
        # show the user profile for that user
        return 'User %s' % username
    else:
        return 'Cannot find %s' % username

@application.route('/group/<int:group_n>')
def show_post(group_n):
    if group_n in [x for x in range(401,412)]:
        return render_template(GROUP_PAGE_TEMPLATE, persons=get_group_list(group_n))
    else:
        return 'Illegal group number: %d' % group_n
    
    
if __name__ == "__main__":
    print(CLASS99_PEOPLE)
    application.run(debug = True)
    