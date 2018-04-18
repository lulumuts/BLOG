class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lulumutuli:lulu@localhost/blogpost'

config_options ={"production":ProdConfig,"default":DevConfig}
