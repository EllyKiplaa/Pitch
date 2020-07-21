import os

class Config:
    '''
    General configuration parent class
    '''
    

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elly:Access2020@localhost/pitch'
    SECRET_KEY = os.environ.get('SECRET_KEY')

 
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
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elly:Access2020@localhost/pitch2'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}