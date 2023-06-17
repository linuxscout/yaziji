#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  yaziji_config.py
#  

#Database config directory
DB_BASE_PATH = "/var/www/html/yaziji/"
# Logging file
LOGGING_CFG_FILE = "/var/www/html/yaziji/web/config/logging.cfg"
LOGGING_FILE = "/var/www/html/yaziji/web/logs/demo.log"
# in developement True in production False
MODE_DEBUG = True
# ~ MODE_DEBUG = False
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
