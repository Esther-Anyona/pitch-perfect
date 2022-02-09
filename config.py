import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch_perfect'
    SECRET_KEY = b'O\x8aL\x80\xc4s(\xb2<:'
    UPLOADED_PHOTOS_DEST ='app/static/photos'



class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}