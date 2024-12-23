#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  yaziji_config.py
#  
OFFLINE = True
# ~ OFFLINE = False   # hosted localy

# in developement True in production False
#MODE_DEBUG = True
MODE_DEBUG = False

"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv
from .languages import languages

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    FLASK_ENV = environ.get("FLASK_ENV")
    MODE_DEBUG = environ.get("MODE_DEBUG")
    SECRET_KEY = environ.get('SECRET_KEY')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    BABEL_DEFAULT_LOCALE="ar"
    BABEL_TRANSLATION_DIRECTORIES="locales;web/locales"
    BABEL_DOMAIN="messages"
    available_languages = environ.get('LANGUAGES')
    if available_languages:
        lang_codes = [lg.strip() for lg in available_languages.split(",")]
        BABEL_LANGUAGES = {lg:languages.get(lg,lg) for lg in lang_codes}
    else:
        BABEL_LANGUAGES = {
            'ar': "العربية",
            'bn': "বাংলা",
            'de': "Deutsche",
            'en': "English",
            # 'es': "Español",
            # 'fr': "Français",
            # 'id': "Bahasa Indonesia",
            # 'ja': "日本語",
            # 'ku': "كوردى",
            # 'zh': "中文"
        }


class ProdConfig(Config):
    """Production config."""
    FLASK_ENV = "production"
    FLASK_DEBUG = False
    DATABASE_URI = environ.get('PROD_DB_BASE_PATH')
    URL_HOST_PATH = environ.get('PROD_URL_HOST_PATH')
    DIR_HOST_PATH =  environ.get('PROD_DIR_HOST_PATH')
    LOGGING_CFG_FILE = DIR_HOST_PATH +environ.get('PROD_LOGGING_CFG_FILE')
    LOGGING_FILE = DIR_HOST_PATH +environ.get('PROD_LOGGING_FILE')


class DevConfig(Config):
    """Development config."""
    FLASK_ENV = "development"
    FLASK_DEBUG = True
    DATABASE_URI = environ.get('DEV_DB_BASE_PATH')
    URL_HOST_PATH = environ.get('DEV_URL_HOST_PATH')
    DIR_HOST_PATH =  environ.get('DEV_DIR_HOST_PATH')
    LOGGING_CFG_FILE = DIR_HOST_PATH + environ.get('DEV_LOGGING_CFG_FILE')
    LOGGING_FILE = DIR_HOST_PATH + environ.get('DEV_LOGGING_FILE')

class config_factory:
    def __init_(self):
        pass
    @staticmethod
    def facory():
        if Config.FLASK_ENV == "development":
            return DevConfig
        elif Config.FLASK_ENV == "production":
            return ProdConfig
        elif Config.FLASK_ENV == "production":
            return Config

# # config parameters
# # as dict
# # development
# config_table ={
#     # in developement True in production False
#     "MODE_DEBUG": False,
#     # URL HOST
#     # For Testing
# 
#     "URL_HOST_PATH":"http://127.0.0.1:5000",
#     "DIR_HOST_PATH": "..",
# 
#     #Database config directory
#     "DB_BASE_PATH" : "..",
# 
#     # Logging file
#     "LOGGING_CFG_FILE": "../web/config/logging.cfg",
#     "LOGGING_FILE":"../web/logs/demo.log",
# }
# 
# 
# config_online ={
#     # in developement True in production False
#     "MODE_DEBUG":False,
#     # URL HOST
#     # For Testing
#     "URL_HOST_PATH":"https://example.com/yaziji",
#     "DIR_HOST_PATH": "~/public_html/cgi-bin",
# 
#     #Database config directory
#     "DB_BASE_PATH" : "/var/www/html/yaziji/",
#     # Logging file
#     "LOGGING_CFG_FILE": "/yazijy/web/config/logging.cfg",
#     "LOGGING_FILE":"/yazijy/web/logs/demo.log", 
#    
# }
# if OFFLINE:
#     # URL HOST
#     # For Testing
#     URL_HOST_PATH = "http://127.0.0.1:5000"
#     #URL_HOST_PATH = "http://127.0.0.1/yaziji"    
#     # ~ DIR_HOST_PATH = "/var/www/html/yaziji"
#     DIR_HOST_PATH = ".."
# 
#     #Database config directory
#     # ~ DB_BASE_PATH = "/var/www/html/yaziji/"
#     DB_BASE_PATH = ".."
#     # Logging file
#     LOGGING_CFG_FILE = DIR_HOST_PATH +"/web/config/logging.cfg"
#     LOGGING_FILE     = DIR_HOST_PATH +"/web/logs/demo.log" 
# else:
#     # For Production
#     URL_HOST_PATH = "https://example.com/yaziji"
#     DIR_HOST_PATH = "~/public_html/cgi-bin"    
#     #Database config directory
#     DB_BASE_PATH = "/var/www/html/yaziji/"
#     MY    
# 
#     # Logging file
#     LOGGING_CFG_FILE = DIR_HOST_PATH +"/yazijy/web/config/logging.cfg"
#     LOGGING_FILE = DIR_HOST_PATH +"/yazijy/web/logs/demo.log"      
# 
# class Config(object):
#     def __init__(self, config_source=""):
#         
#         self._config = self._load_config(config_source)
#         
#     def get_property(self, property_name):
#         if property_name not in self._config.keys(): # we don't want KeyError
#             return None  # just return None if not found
#         return self._config[property_name]
#         
#     def _load_config(self, config_source =""):
#         """
#         Load config from source
#         """
#         if not config_source:
#             self._config = config_table # set it to conf
#         elif type(config_source)==dict:
#             self._config = config_source # set to a specific dict
#         #TODO: config from file
#         elif type(config_source)==str:
#             self._config = config_table# to be handled
#         else:
#             self._config = config_table # default case
#         return self._config
# 
# class webConfig(Config):
# 
#     def __init__(self, config_source =""):
#         Config.__init__(self, config_source=config_source)
# 
#     @property
#     def url_host_path(self):
#         return self.get_property("URL_HOST_PATH")
#         
#     @property
#     def dir_host_path(self):
#         return self.get_property("DIR_HOST_PATH")
#         
#     @property
#     def db_base_path(self):
#         """Database config directory"""        
#         return self.get_property("DB_BASE_PATH")
#                 
#         
#     @property
#     def logging_cfg_file(self):
#         """ Logging file config file
#         """
#         return self.get_property("LOGGING_CFG_FILE")
#         
#     @property
#     def logging_file(self):
#         """ Logging file 
#         """
#         return self.get_property("LOGGING_FILE")\
# 
#     @property
#     def mode_debug(self):
#         """ Logging file
#         """
#         return self.get_property("MODE_DEBUG")

def main(args):
    # cfg1 = Config()
    # # assert(cfg1.get_property("LOGGING_FILE")=="/web/logs/demo.log")
    # cfg = webConfig()
    # print(dir(cfg))
    # print(cfg._config)
    # print(cfg.logging_file)
    # print(cfg)
    print(Config.BABEL_LANGUAGES)
    myconf = config_factory.facory()
    print(myconf.__name__,myconf.FLASK_DEBUG, myconf.FLASK_ENV)
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
