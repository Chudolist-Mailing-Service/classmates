# -*- coding: utf-8 -*-
import yaml
import chardet
import codecs

from flask import Flask, render_template
from operator import itemgetter

application = Flask("application")
main_page_tamplate_file = "table.html"


def loadfile(name, encoding=None, **kwargs):
    with open(name, 'rb') as content_file:
        content = content_file.read()  # type: bytes
        cd = chardet.detect(content)
    enc = encoding or cd.get('encoding', 'ascii')

    return yaml.load(content.decode(enc), **kwargs)

def dumps(data, encoding=None, **kwargs):
    res = yaml.dump(data, **kwargs)
    if encoding:
        return codecs.unicode_escape_decode(res)[0].encode(encoding)
    return res

def get_classmates(file='classmates.txt', pivot='name'):
    classmates = loadfile(file)
    return sorted(classmates, key=itemgetter(pivot))
    
@application.route("/")
def hello():
    classmates = get_classmates()
    return render_template(main_page_tamplate_file, persons=classmates)

if __name__ == "__main__":
    application.run()
