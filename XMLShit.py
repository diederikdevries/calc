from dict2xml import dict2xml

import requests     

auth = {            
  "user": {
    "username": "myemail@mydomain.com",
    "key": "90823ff08409408aebcf4320384"
  }
}

print(type(auth))
print (dict2xml(auth))
