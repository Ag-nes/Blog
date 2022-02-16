import os 

class Config:
    '''
    '''
    SECRET_KEY='SECRET_KEY'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://agnes:powers123@localhost/powerposts'
    UPLOADED_PHOTOS_DEST='app/static/photos'

    #email config
    MAIL_SERVER = 'faithagnes2@gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("faithagnes2@gmail.com")
    MAIL_PASSWORD = os.environ.get("@liammyfirst1")

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

    DEBUG=True

config_options={
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}