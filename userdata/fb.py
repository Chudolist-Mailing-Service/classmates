# -*- coding: utf-8 -*-
import facebook

TOKEN = "EAACEdEose0cBACcqYnLeMoX7r9FZA8IJScFVNsRrjjUQkEpVROrPWZBcZBZBobNZAa5E3cZBBJVmcMJevvv5NnOrR8vTFkZBy6b9vFZCfu7kZAnh0bEOgijGOvqsUTZBZAeZBk665iTkAtfcSNgULFUd1NAvq6Oazk70jgCrqMr41RZAV6AZDZD"

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
Svetlana  Shmykova
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




graph = facebook.GraphAPI(access_token=TOKEN)
members = graph.get_object(id='140514919349870/members')
print(C_NAMES)
for m in members['data']:
    name = m['name']
    if name in C_NAMES:
        #print("---")
        #print("- " + m['name'])
        #print("- " + m['id'])
        #print("- " + m['name'])
        print("\t".join([m['name'], m['id']]))
        C_NAMES.pop(C_NAMES.index(name))
assert len(C_NAMES) == 1
assert C_NAMES == ['Evgeny Rybin']

my =  graph.get_object(id='me/friends')

yaml_docs = """---
- Pogrebnyak Evgeny
- 140514919349870
- Погребняк Евгений
---
- Михаил Хромов
"""

csv= "Погребняк\tЕвгений\tВладимирович\t"

import yaml
print ([x for x in yaml.load_all(yaml_docs)])
