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

# {'translit': 'Taljantsev_Sergej_410',
#      'name': 'Тальянцев Сергей',
#     'group': '410',
#       'url': 'https://www.facebook.com/1029131133789392' }

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
        # order list by group and name
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

       # if above does not work:
       #for z in self.people:
       #   if translit_name == z['translit']:
       #      z['url'] = url

       # add to file REGISTERED_USERS_JSON_PATH
       self.registered_facebook_ids[translit_name] = url
       dump_to_json(self.registered_facebook_ids, REGISTERED_USERS_JSON_PATH)

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
    dump_to_json(TEST_DUMMY_DICT, REGISTERED_USERS_JSON_PATH)
    assert TEST_DUMMY_DICT             == Classmates().get_class()[1]
    assert TEST_DUMMY_DICT['translit'] == Classmates().get_translit_names()[1]
    assert TEST_DUMMY_DICT             == Classmates().get_user(TEST_DUMMY_DICT['translit'])
    assert 25                          == len(Classmates().get_group(410))
    r = Classmates()
    mock_id = '1234567892'
    mock_url = 'https://www.facebook.com/' + mock_id
    r.set_facebook_id('LastName_FirstName_400', mock_id)
    assert mock_url == r.get_user('LastName_FirstName_400')['url']
    assert mock_url == Classmates().get_user('LastName_FirstName_400')['url']
    