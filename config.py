##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
