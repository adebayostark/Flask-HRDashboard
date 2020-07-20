class Config(object):
    """Base configuration setting"""
    DEBUG = True
    SECRET_KEY = '\xd8\x04\x9e2C\xe2\x90\x9a\x01\\%\x04\x95feW\x96\xb4K\x0c\x034\x1cS'
    SQLALCHEMY_DATABASE_URI= 'sqlite:///application.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = 'app/static/uploads'
class ProdConfig(Config):
    """Production configuration setting"""
    DEBUG = False
class DevConfig(Config):
    """Development configuration setting"""
    DEBUG = True
class TestConfig(Config):
    """Testing configuration setting"""
    DEBUG = True
    TESTING=True
    