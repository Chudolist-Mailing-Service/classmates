# -*- coding: utf-8 -*-
import yaml
import chardet
import codecs

from flask import Flask, render_template
from operator import itemgetter

application = Flask("application")
MAIN_PAGE_TEMPLATE_FILE = "table.html"
YAML_SOURCE_FILE = 'classmates.txt'

def loadfile(name, encoding=None):
    """Guess encoding and load yaml data from file."""
    with open(name, 'rb') as content_file:
        content = content_file.read()  # type: bytes
        cd = chardet.detect(content)
    enc = encoding or cd.get('encoding', 'ascii')
    return yaml.load(content.decode(enc))

def dumps(data, encoding=None):
    """Dumps yaml data to file with spcified encoding.""" 
    res = yaml.dump(data)
    if encoding:
        return codecs.unicode_escape_decode(res)[0].encode(encoding)
    return res

def get_classmates(file=YAML_SOURCE_FILE):
    return loadfile(file)
    
@application.route("/")
def hello():
    classmates = get_classmates()
    return render_template(MAIN_PAGE_TEMPLATE_FILE, persons=sorted(classmates, key=itemgetter('name')))

if __name__ == "__main__":
    application.run()
