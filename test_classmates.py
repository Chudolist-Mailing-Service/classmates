from classmates import Classmates

TEST_DUMMY_DICT = {'translit': 'LastName_FirstName_400', 
                  'group': '400', 
                    'url': '', 
                   'name': '_Фамилия1 _Имя1'}

def test_init1():    
    test_user = Classmates().get_user(TEST_DUMMY_DICT['translit'])                   
    for ks in ['translit', 'group', 'name']:
        assert TEST_DUMMY_DICT[ks] == test_user[ks] 
        
def test_init2():
    # WARNING: test may fail upon update of classmates.json    
    test_user = Classmates().get_user(TEST_DUMMY_DICT['translit'])                       
    dummy_index = 1 # can also be 0, some lost entry is now at position 0                       
    assert test_user == Classmates().get_class()[dummy_index]
    assert TEST_DUMMY_DICT['translit'] == Classmates().get_translit_names()[dummy_index]

def test_group():    
    assert 25 == len(Classmates().get_group(410))
    
    
    
def test_uodate():    
    r = Classmates()
    mock_id = '1234567892' # todo: make this a random number, pervious number is already in classmates.json, better test with a new value 
    mock_url = 'https://www.facebook.com/' + mock_id
    r.set_facebook_id('LastName_FirstName_400', mock_id)
    assert mock_url == r.get_user('LastName_FirstName_400')['url']
    assert mock_url == Classmates().get_user('LastName_FirstName_400')['url']
    