""" Configuration file for the API """
import os

class Config(object):
    """ Parent configuration class """
    DEBUG = False
    TESTING = False
    SECRET = os.getenv('SECRET')
    JWT_SECRET_KEY=os.getenv('JWT_SECRET_KEY')
    
class DevelopmentConfig(Config):
    """ Configuration for development environment """
    DEBUG = True
    DATABASE_URL=os.getenv('DATABASE_URL')
    
class TestingConfig(Config):
    """ Configuration for the testing environment """
    TESTING = True
    DEBUG = True
    DATABASE_URL=os.getenv('TEST_DATABASE_URL')

class ProductionConfig(Config):
    """ Configuration for the production environment """
    DEBUG = False
    TESTING = False

APP_CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

