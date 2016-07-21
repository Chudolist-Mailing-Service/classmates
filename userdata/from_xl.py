import xlrd
import os
import csv
import json

XL_PATH = os.path.join('classmates.xls')
FMT = {'delimiter':';', 'lineterminator':"\n"}

def read_from_csv(filename, fieldnames):
    with open(filename, 'r') as csvfile:
        for x in csv.DictReader(csvfile, fieldnames=fieldnames,**FMT):
            yield x

def get_ids():
    iterable = read_from_csv(filename='ids.csv',fieldnames=['fb_name','id'])
    return {x['fb_name']:x['id'] for x in iterable}

def get_full_classlist():
    rb = xlrd.open_workbook(XL_PATH)
    sheet = rb.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        row = sheet.row_values(rownum)
        yield(row)

def get_printable():
    d = get_ids()
    for x in get_full_classlist():
        if x[0] and x[4]:
            yield {'name': ' '.join([x[0],x[1]]).strip(),
                    'url':"https://www.facebook.com/" + d[x[4]] 
                   }
            
if __name__ == "__main__":

  a = list(get_printable())
  
  with open('classmates.json', 'w') as file:
      json.dump(a,file)
      
  with open('classmates.json', 'r') as file:
      b = json.load(file)
      
      
  assert a == b