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

import yaml

FB_PREFIX = "https://www.facebook.com/"

with open('classmates.txt', 'r') as stream:
   print(yaml.load(stream))
 
# currently get an error:  
# yaml.scanner.ScannerError: mapping values are not allowed here
# in "classmates.txt", line 2, column 5
