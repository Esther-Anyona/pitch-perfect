import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch_perfect'
    SECRET_KEY = b'O\x8aL\x80\xc4s(\xb2<:'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_USERNAME = "smtpesther@gmail.com"
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_PASSWORD ="smtp12345"


class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    pass
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch_perfect'
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}