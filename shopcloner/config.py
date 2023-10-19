import json
import os

class Config : 

    def __init__(self, login_url, username, password,ProductUrl):
        self._login_url = login_url
        self._username = username
        self._password = password
        self._product_url = ProductUrl


    @property
    def LoginUrl(self):
        return self._login_url
    
    @property
    def Username(self):
        return self._username
    
    @property
    def Password(self):
        return self._password

    @property
    def ProductUrl(self):
        return self._product_url
    


class ConfigFactory:

    @staticmethod
    def GetConfig() -> Config:

        config_file = open(os.path.join( os.path.abspath(''),'config.json' ))

        config_dict = json.load(config_file)

        config = Config(
            config_dict['LoginUrl'], 
            config_dict['Username'], 
            config_dict['Password'],
            config_dict['ProductUrl'])

        return config
    


