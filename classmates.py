#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Read classmates data from json, display as full list, by group or as individual page.
   Also allows to collect missing information about classmates FB ids. 
"""

#TODO:
#- fix 412 group error 
#- create explicitly classmates.json (from csv, csv really better)
#- make jsons readable
#- review this file ("model")

#- list of photos by group
#- analyze graph of friends: 
#    find classmates not listed   
#    most connected group 
#    complete group
#    friendliest person
# - "Найди меня"
# - внутренний messenger - авторизовать рассылку на почту


import json
from transliterate import translit
from operator import itemgetter

CLASSMATES_JSON_PATH = 'classmates.json'
REGISTERED_USERS_JSON_PATH = 'registered_users.json'
TEST_DUMMY_DICT = {'translit': 'LastName_FirstName_400', 'group': '400', 'url': '', 'name': '_Фамилия1 _Имя1'} 

# {'translit': 'Taljantsev_Sergej_410', 'name': 'Тальянцев Сергей', 'group': '410', 'url': 'https://www.facebook.com/1029131133789392'}

def read_json(filename):
   """Return data imported from json."""
   with open(filename, 'r') as file:
      return json.load(file)

def dump_to_json(data, filename):
   with open(filename, 'w') as outfile:
      json.dump(data, outfile)

class Classmates():
   def __init__(self):
        self.people = self.load_classmates()
        
        # TODO: 
        # read registered_users.json
        self.registered_facebook_ids = read_json(REGISTERED_USERS_JSON_PATH)
        # replace urls in self.people for registered users 
        for p in self.people:
           name = p['translit']
           if name in self.registered_facebook_ids.keys():
              p['url'] = self.registered_facebook_ids[name]
        # may also dump final full json 
        dump_to_json(data, 'full_list.json')
        
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
        people = read_json(CLASSMATES_JSON_PATH)
        
        # THIS CAN GO TO DATA PREPARATON ---------------------------------------------
        #add translit name 
        for p in people:        
            p['translit'] = self._to_latin(p['name']) + "_" + p['group']    
        # add dummy for testing
        test_user_dict = {'translit': 'LastName_FirstName_400', 'group': '400', 'url': '', 'name': '_Фамилия1 _Имя1'} 
        people = [test_user_dict] + people  
        # END - THIS CAN GO TO DATA PREPARATON ---------------------------------------------
        
        # order list by proup and name
        return sorted(people,key=itemgetter('group', 'name'))

   def get_group_list(self, group_n:int):
        if isinstance(group_n, int):
            return [p for p in self.people if p['group'] == str(group_n)]
        else:
            raise TypeError(group_n)
        
   def get_user(self, translit_name):
        return [p for p in self.people if p['translit'] == translit_name][0]  
        
   def add_facebook_id(translit_name, user_id):
       # add to self.people
       
       # option 1
       # url = "https://www.facebook.com/" + user_id
       # p = self.get_user(translit_name)
       # p['url'] = url
       
       #
       #for z in self.people:
       #   if translit_name == z['translit']:
       #      z['url'] = url
       
       # add to REGISTERED_USERS_JSON_PATH
       
       # add to self.registered_facebook_ids
       # {translit_name:url}
       
       # dump self.registered_facebook_ids to json 
       pass
    

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
    assert TEST_DUMMY_DICT             == Classmates().get_people()[0]
    assert TEST_DUMMY_DICT['translit'] == Classmates().get_translit_names()[0]
    assert TEST_DUMMY_DICT             == Classmates().get_user(TEST_DUMMY_DICT['translit'])
    assert 25                          == len(Classmates().get_group_list(410)) 
    
