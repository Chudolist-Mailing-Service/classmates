Classmates - flask app holding a list of classmates:

<http://chudoclass.us-west-2.elasticbeanstalk.com/>

URLs:
  - <http://52.43.77.82>
  - <http://chudoclass.us-west-2.elasticbeanstalk.com>
  - <https://github.com/epogrebnyak/classmates>

TODOs:
-----
	 
    Основные вопросы:
	- как ветку get-fb-id сделать мастером? нужно мерджить как-то или переставить HEAD на get-fb-id надо?
	  или вообще как-то не так?
	  
    - чтобы заработало в AWS - нужно поменять
    
      # FACEBOOK_CALLBACK = 'http://localhost:5000/oauth/callback/facebook'
      FACEBOOK_CALLBACK = "http://chudoclass.us-west-2.elasticbeanstalk.com/oauth/callback/facebook"
      
	  или нужны еще какие-то изменения, с токенами, например? сейчас токены работают только для локальной версии?
	  
    - сделан класс Classmates() в classmates.py - это модель данных. 
	   - есть ли по нему какие-то замечания и предложения?
	   - правильно ли считать что url это views, а POST запросы (нажать кнопку) это контроллер? или все как-то сложнее?
	
    - сделаны тесты для модели данных (test_classmates.py), какие есть подходы к тестированию views и особенно 
	  контроллера? что и как там проверяют?
    
    Minor:
    - [ ] Лучич Беляна in userdata, list on screen and in test
    - [ ] put userdata with excel to private repo for creating classmates.json   
      
    Soon:
    - like button for entire page
    - [ ] store and show person's photo
    - domain name chudoclass.ru    
    - nicer html templates
    - more testing
    
    Not soon:
    - linkedin, vkontakte links
    - extendible to other MSU Econ classes
    
    MORE FB FEATURES:
	```
    #- analyze graph of friends:
    #    find classmates not listed
    #    most connected group
    #    complete group
    #    friendliest person
    # - "Найди меня" - список кого мы не видим в соцсетях
    # - авторизовать почту или сообщения в мессенджере   
    ```
    