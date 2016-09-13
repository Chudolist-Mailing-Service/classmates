Classmates - flask app holding a list of classmates:

<http://chudoclass.us-west-2.elasticbeanstalk.com/>

URLs:
  - <http://52.43.77.82>
  - <http://chudoclass.us-west-2.elasticbeanstalk.com>
  - <https://github.com/epogrebnyak/classmates>

TODOs:
-----

TODOs:
	 
    Major:
    - [ ] app in AWS - deploy this to AWS - must change
    
      FACEBOOK_CALLBACK = 'http://localhost:5000/oauth/callback/facebook'
      FACEBOOK_CALLBACK = "http://chudoclass.us-west-2.elasticbeanstalk.com/oauth/callback/facebook"
  
    - [ ] model is Classmates(), veiws are app urls and controller is POST function? what else should be done in MVC?
    - [ ] we have tests for data model (test_classmates.py), but what are tests for views and controller like?
    
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
    