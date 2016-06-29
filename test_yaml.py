from application import get_classmates 

CLASSMATES = [
    {
        'name': 'Громова Дарья',
        'url': 'https://www.facebook.com/gromova.da'
    },
    {
        'name': 'Слободник Алексей',
        'url': 'https://www.facebook.com/markus.duck.90'
    },
    {
        'name': 'Каминский Денис',
        'aff': 'fut.ru',
        'url': 'https://www.facebook.com/dennis.kaminsky.3'
    },
    {
        'name': 'Головизнин Алексей',
        'aff': 'Кант',
        'url': 'https://www.facebook.com/AirVetra'
    },
    {
        'name': 'Кузнецова (Ромашова) Екатерина',
        'aff': 'РФПИ',
        'url': 'https://www.facebook.com/kate.romashova'
    }
]

classmates = get_classmates(file = "test_yaml.txt")

def test_import():
    assert len(classmates) == len(CLASSMATES)
    for c, C in zip(classmates, CLASSMATES):
        assert C == c