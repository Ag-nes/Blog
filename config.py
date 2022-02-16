import os 

class Config:
    '''
    '''
    SECRET_KEY='SECRET_KEY'
    UPLOADED_PHOTOS_DEST='app/static/photos'

    #email config
    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProductionConfig(Config):
    '''
    '''
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # or other relevant config var
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    # rest of connection code using the connection string `uri`

    

class DevelopmentConfig(Config):
    '''
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://agnes:powers123@localhost/powerposts'

    DEBUG=True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}