import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch_perfect'



class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}