#   Python File for defining the application configuration properties
class appConfig():
    #---app configuration properties---
    DEBUG = True
    TESTING = False

    #---flask sqlalchemy configuration properties---
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI="sqlite:///data.db"

    #---flask security configuration properties---
    SECURITY_LOGOUT_URL = '/logout'
    SECRET_KEY = "thisissecretkey"
    SECURITY_PASSWORD_SALT = "thisissalt"
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'authentication-token'
    SECURITY_TOKEN_MAX_AGE = 3600

    