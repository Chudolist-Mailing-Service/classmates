# -*- coding: utf-8 -*-
"""Read classmates data from json, display as full list, by group or as individual page.
   Also allows to collect missing information about classmates FB ids. 
"""

import json
from flask import Flask, render_template
from operator import itemgetter

# will require update to req.txt
from transliterate import translit

application = Flask("application")
<<<<<<< HEAD
MAIN_PAGE_TEMPLATE_FILE = "table.html"
CLASSMATES_JSON_PATH = os.path.join('classmates.json')
=======
>>>>>>> origin/master

MAIN_PAGE_TEMPLATE  = "table.html"
GROUP_PAGE_TEMPLATE = "group.html"
USER_PAGE_TEMPLATE  = "user.html"

CLASSMATES_JSON_PATH = 'classmates.json'

def get_classmates():
    """Return list of dictionaries holding classmates data."""
    
    def _to_latin(s):
        """Transliterate Russian into Latin charaters."""
        return translit(s, 'ru', reversed=True).replace(" ", "_").replace("'","") 

    #load data from json
    with open(CLASSMATES_JSON_PATH, 'r') as file:
        people = json.load(file)    

    #add verson of translit name 
    for p in people:        
        p['translit'] = _to_latin(p['name']) + "_" + p['group']    

    # add dummy for testing
    test_user_dict = {'translit': 'LastName_FirstName_400', 'group': '400', 'url': '', 'name': '_Фамилия1 _Имя1'} 
    people = [test_user_dict] + people  

    # order list by proup and name
    return sorted(people,key=itemgetter('group', 'name'))

    
PEOPLE = get_classmates()
TRANSLIT_NAMES = [p['translit'] for p in PEOPLE]

def get_group_list(group_n):
    return [p for p in PEOPLE if p['group'] == str(group_n)]
    
def pick_dict_by_translit(translit_name):
    return [p for p in PEOPLE if p['translit'] == translit_name][0]  
        
@application.route("/")
def hello():      
<<<<<<< HEAD
    classmates = sorted(get_classmates(),key=itemgetter('group'))
    return render_template(MAIN_PAGE_TEMPLATE_FILE, persons=classmates)
=======
    return render_template(MAIN_PAGE_TEMPLATE, persons=PEOPLE)
>>>>>>> origin/master

    
@application.route('/user/<username>')
def show_user_profile(username):         
    if username in TRANSLIT_NAMES:
        p = pick_dict_by_translit(username)
        return render_template(USER_PAGE_TEMPLATE, person=p)        
    else:
        return 'Cannot find %s' % username

@application.route('/group/<int:group_n>')
def show_post(group_n):
    if group_n in [x for x in range(401,412)]:
        return render_template(GROUP_PAGE_TEMPLATE, persons=get_group_list(group_n))
    else:
        return 'Illegal group number: %d' % group_n
    
    
if __name__ == "__main__":
<<<<<<< HEAD
    print(sorted(get_classmates(),key=itemgetter('group', 'name')))
=======
    print("""TODO:
    Major:
    - collect missing FB id information    
    - data collection scripts 
    - redeploy from git directory with new requirements.txt        
    
    Minor:
    - add 401...411 to list/group view + all buttons
    
    Soon:
    - big like button FS
    - store and show person's photo
    - domain name      
    - linkedin, vkontakte links
    - nice htmls overall and template structure
    - testing
    
    Not soon:
    - extendible to other MSU Econ classes
    - storing personal information securely
    
    """)
>>>>>>> origin/master
    application.run(debug = True)
    