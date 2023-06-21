#!/usr/bin/python3
import sys
import os
from wsgiref.handlers import CGIHandler
sys.path.insert(0,"yazijy/webfrontend/")
#sys.path.insert(0,"/home/tahadz/public_html/cgi-bin/yazijy/web/")
sys.path.insert(0,"yazijy/web/")
sys.path.insert(0,"yazijy/yaziji/")
import cgitb
cgitb.enable(logdir=os.path.join(os.path.dirname(__file__), 'tmp/logs'),
            display=True, format='html',)

from yaziji_webserver import app

os.environ["REQUEST_METHOD"] = "GET"; 

#print("Content-Type: text/html\n\n")
#print("Hello, worldi Taha3 !\n")
CGIHandler().run(app)


