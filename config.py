import os

class Config:
    '''
    General configuration parent class
    '''
    

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elly:Access2020@localhost/pitch'

 
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
    Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elly:Access2020@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}