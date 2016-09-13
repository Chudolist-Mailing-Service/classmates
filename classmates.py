#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Read classmates data from two jsons, get it as full list, by group or retrive individual user.
   Also allows to udate user facebook ids.
   
   Original hardcoded user data stored in: classmates.json   
   New data, obtained interactively stored in: registered_users.json
"""

import json
from transliterate import translit
from operator import itemgetter

CLASSMATES_JSON_PATH = 'classmates.json'
REGISTERED_USERS_JSON_PATH = 'registered_users.json'

def read_json(filename):
   """Return data imported from json."""
   with open(filename, 'r') as file:
      return json.load(file)

def dump_to_json(data, filename):
   with open(filename, 'w') as outfile:
      json.dump(data, outfile, indent=4, separators=(',', ': '))

class Classmates():
   def __init__(self):

        #load data from main json
        self.people = read_json(CLASSMATES_JSON_PATH)
        # order it by group and name
        self.people = sorted(self.people,key=itemgetter('group', 'name'))

        # read registered users json
        self.registered_facebook_ids = read_json(REGISTERED_USERS_JSON_PATH)
        # replace urls in self.people for registered users
        for p in self.people:
           name = p['translit']
           if name in self.registered_facebook_ids.keys():
                p['url'] = self.registered_facebook_ids[name]

   def get_class(self):
        return self.people

   def get_group(self, group_n:int):
        if isinstance(group_n, int):
            return [p for p in self.people if p['group'] == str(group_n)]
        else:
            raise TypeError(group_n)

   def get_user(self, translit_name):
        # Return entry like below:
        #
        # {'translit': 'Taljantsev_Sergej_410', 
        #      'name': 'Тальянцев Сергей',
        #     'group': '410',
        #       'url': 'https://www.facebook.com/1029131133789392' }
        #
        return [p for p in self.people if p['translit'] == translit_name][0]

   def get_translit_names(self):
       return [p['translit'] for p in self.people] 
   
   def set_facebook_id(self, translit_name, user_id):
       # add information to self.people
       url = "https://www.facebook.com/" + user_id
       p = self.get_user(translit_name)
       if p:
           p['url'] = url
       else:
           raise ValueError("Cannot assign url to missing user: " + translit_name) 

       # add new data to file REGISTERED_USERS_JSON_PATH
       self.registered_facebook_ids[translit_name] = url
       dump_to_json(self.registered_facebook_ids, REGISTERED_USERS_JSON_PATH)