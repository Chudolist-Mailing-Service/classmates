# -*- coding: utf-8 -*-

C_NAMES = """Dmitry Shmelev
Hayk Safaryan
Yulia Trofimova
Markus Duck
Andrey Teryoshin
Alex Naz
Dmitry Ivanov
Oleg Maz
Anton Volodkin
Tatiana Medvedeva
Павел Одеров
Sergey  Mikhailov
Dinara Aktasheva
Ирина Шинкаренко
Ruslan Sibaev
Ksenia Maiboroda
Alina  Kolankova
Nikolay  Tkachenko
Oxana Volkova
Мария Милоградова
Roman Kashcheyev
Evgeny Rybin
Kirill  Kutyrin
Дарья Брожовская
Yulia  Melnikova
Ivan  Efimov
Ekaterina Koukhto
Nataly Di
Елена Володина
Stan Bukanov
Dmitry Barashkov
Anna  Avramenko
Lena Kiseleva
Andrey Mikhaylov
Dmitry  Samoylov
Natalia Safronova
Катя Тру
Ирина Прозорова
Nadezhda Ponomareva
Anastasia Vishnevskaya
Sergey  Krasnov
Ekaterina Kafarova
Sylvia Peshich
Алексей Манченко
Ксения Нечаева
Elena Kiseleva
Anna Ivkovic
Artemy Izmestiev
Sergey Volzhin
Евгения Стефанович Ех. Дементьева
Arina Arisha
Ekaterina Reshetnikova
Anna Guseva
Catrina Yunkevich
Semen Zherder
Ivan Glinkin
Svetlana Kosheleva
Elena Vodopianova
Ekaterina Kolesnikova
Safiullina Dinara
Levan  Ninikashvili
Ivan Safronov
Liza Polyakova
Сергей Полевой
Алексей Юнкевич
Elvira Temirova
Кирилл Каленик
Andrey Bobyshev
Olga Moroz
Andrey Leonov
Sergey Bogdanov
алексей пономарев
Михаил Ку
Marat  Bogatyrev
Anna Chernyaeva
Sergey Taliyantsev
Anton Pospelov
Anna Stark
Marina Kamchatnova
Olga Grits
Anastasia Santja
Sergey Solntsev
Don Schedro
Alexey  Markov
Katya Fradkina
Anna Bogomolova
Irina Eltsova
Dmitry Pluschev
Mikhail Zak
Ivliev Artem
Julia Kim
Igor Voskanyan
Anna Belyaeva
Elena Kozlovskaya
Basil Basill
Andrei Pl
Maria Malkova
Alexey Klsh
Oleg Dolgov
Anna Belomestnova
Dennis Kaminsky
Alexey Goloviznin
Katya Kuznetsova
Asatur Gukasyan
Irina Kroo
Дарья Громова
Abakhon Sultonnazarov
Alexander Tereshchenko
Nataly Tsakirova
Яна Богдановская
Evgeny Yankovoy
Den Bo
Olga Ievleva-Stark
Sergey Barabanov
Ольга Молчанова
Михаил Хромов
Oksana Staroselskaya
Михаил Коротков
Mikhail Ivanov
Pogrebnyak Evgeny""".split('\n')

import csv
import facebook

TOKEN = "EAACEdEose0cBAHol1C7LS3B3pbulDG3AF02HZAZA5ikoNHeWf0VJxMOZBhZAwNXHVlAkWNmDSwKUvrLLTUdRcZCwdekJ07EpcgeUl1hZBivukmNrkWwL24yZAJbLc8BX0LKX07U5ZC9PBEJlexqnPavDDMBWDqoaHbHv01u9LukMjgZDZD"
G_ID = '140514919349870/members'
FMT = {'delimiter':';', 'lineterminator':"\n"}


# get classmates from chudolist group 
def yeild_classmates_from_group(access_token=TOKEN, 
                                group_id=G_ID,
                                names=C_NAMES):

    graph = facebook.GraphAPI(access_token)
    members = graph.get_object(id=group_id)
    for m in members['data']:
        name = m['name']
        if name in names:
            yield m['name'], m['id']


def save_to_csv(filename, iterable):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, **FMT)    
        writer.writerows(iterable)

def read_from_csv(filename):
    with open(filename, 'r') as csvfile:    
        return list(csv.reader(csvfile, **FMT)) 

if __name__ == "__main__": 
  save_to_csv(filename="_temp_ids_from_chudolist_group.csv", iterable=yeild_classmates_from_group())       
  k = read_from_csv('ids.csv')
        
