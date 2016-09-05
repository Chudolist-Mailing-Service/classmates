#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Read classmates data from json, display as full list, by group or as individual page.
   Also allows to collect missing information about classmates FB ids. 
"""

import json
from transliterate import translit
from operator import itemgetter

CLASSMATES_JSON_PATH = 'classmates.json'
TEST_DUMMY_DICT = {'translit': 'LastName_FirstName_400', 'group': '400', 'url': '', 'name': '_Фамилия1 _Имя1'} 

{'translit': 'Streltsova_Polina_412', 'name': 'Стрельцова Полина', 'group': '412', 'url': ''}
{'translit': 'Taljantsev_Sergej_410', 'name': 'Тальянцев Сергей', 'group': '410', 'url': 'https://www.facebook.com/1029131133789392'}

class Classmates():
    def __init__(self):
        self.people = self.load_classmates()
        
    def get_people(self):
        return (self.people)
    
    def get_translit_names(self):
        return [p['translit'] for p in self.people]    
        
    def _to_latin(self, s):
        """Transliterate Russian into Latin charaters."""
        return translit(s, 'ru', reversed=True).replace(" ", "_").replace("'","") 
        
    def load_classmates(self):
        """Return list of dictionaries holding classmates data."""
        #load data from json
        with open(CLASSMATES_JSON_PATH, 'r') as file:
            people = json.load(file)    
        #add translit name 
        for p in people:        
            p['translit'] = self._to_latin(p['name']) + "_" + p['group']    
        # add dummy for testing
        test_user_dict = {'translit': 'LastName_FirstName_400', 'group': '400', 'url': '', 'name': '_Фамилия1 _Имя1'} 
        people = [test_user_dict] + people  
        # order list by proup and name
        return sorted(people,key=itemgetter('group', 'name'))

    def get_group_list(self, group_n:int):
        if isinstance(group_n, int):
            return [p for p in self.people if p['group'] == str(group_n)]
        else:
            raise TypeError(group_n)
        
    def get_user(self, translit_name):
        return [p for p in self.people if p['translit'] == translit_name][0]  

# def show_user_profile(username):         
    # if username in TRANSLIT_NAMES:
        # p = pick_user_by_translit(username)
        # session['username'] = username
        # return render_template(USER_PAGE_TEMPLATE, person=p)        
    # else:
        # return 'Cannot find %s' % username

# def show_post(group_n):
    # if group_n in [x for x in range(401,412)]:
        # return render_template(GROUP_PAGE_TEMPLATE, persons=get_group_list(group_n))
    # else:
        # return 'Illegal group number: %d' % group_n
    
    # session['facebook_token'] = (resp['access_token'], '')
    # me = facebook.get('/me?fields=id')
    # u_id = me.data['id']

    # url = "https://www.facebook.com/" + u_id
    # p = pick_user_by_translit(session['username'])
    # p['url'] = url

    # new_data = [user if user['translit']!=session['username'] else p for user in PEOPLE]

    # with open('classmates.json', 'w+') as outfile:
        # json.dump(new_data, outfile)

if __name__ == "__main__":
    z = Classmates()
    assert TEST_DUMMY_DICT             == Classmates().get_people()[0]
    assert TEST_DUMMY_DICT['translit'] == Classmates().get_translit_names()[0]
    assert TEST_DUMMY_DICT             == Classmates().get_user(TEST_DUMMY_DICT['translit'])
    assert 25                          == len(Classmates().get_group_list(410)) 
    




