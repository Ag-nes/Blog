import os 

class Config:
    '''
    '''
    SECRET_KEY='SECRET_KEY'
    UPLOADED_PHOTOS_DEST='app/static/photos'

    #email config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProductionConfig(Config):
    '''
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

class DevelopmentConfig(Config):
    '''
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://agnes:powers123@localhost/powerposts'

    DEBUG=True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}