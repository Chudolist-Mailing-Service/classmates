# -*- coding: utf-8 -*-

CLASSMATES = [
{  'name':'Громова Дарья',
    'url':'https://www.facebook.com/gromova.da'
},

{ 
  'name':'Слободник Алексей',
   'url':'https://www.facebook.com/markus.duck.90'
   },

{ 
  'name':'Головизнин Алексей',
   'url':'https://www.facebook.com/AirVetra'
  },

{ 
  'name':'Каминский Денис',
   'url':'https://www.facebook.com/dennis.kaminsky.3',
   'aff':'fut.ru'
},

{
  'name':'Кузнецова (Ромашова) Екатерина',
   'url':'https://www.facebook.com/kate.romashova',
 }
] 

from flask import Flask, render_template
application = Flask("application")

from operator import itemgetter

@application.route("/")
def hello():
    return render_template("table.html", persons=sorted(CLASSMATES, key=itemgetter('name')))
     

if __name__ == "__main__":

    application.run()