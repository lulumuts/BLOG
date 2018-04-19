import os

class Config:
    pass
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lulumutuli:lulu@localhost/blogpost'

config_options ={"production":ProdConfig,"default":DevConfig}
