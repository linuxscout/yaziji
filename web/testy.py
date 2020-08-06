#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import sys
from bottle import Bottle, run
from bottle import static_file
from bottle import template
from bottle import view
from bottle import get
from bottle import request
from bottle import response
from bottle import TEMPLATE_PATH

import json
import os.path
import datetime
import logging
import adaat
app = Bottle()
WEB_PATH = os.path.dirname(os.path.realpath(__file__))
TEMPLATE_PATH.insert(0, os.path.join(WEB_PATH, "views"))

# define logger
# prepare logging 
d = os.path.dirname(sys.argv[0])
LOG_FILENAME = os.path.join(d,u'tmp','logging_yaziji.out')
logging.basicConfig(filename = LOG_FILENAME,level=logging.INFO,)
myLogger = logging.getLogger('Mishkal')
h = logging.StreamHandler() # in production use WatchedFileHandler or RotatingFileHandler
h.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
myLogger.addHandler(h)
myLogger.setLevel(logging.INFO) # in production use logging.INFO
#~ myLogger.setLevel(logging.DEBUG) # in production use logg
def writelog(text,action):
    """
    @param text: an object to be logged
    @type text: object
    """
    timelog = datetime.datetime.now().strftime("%Y-%m-%d %I:%M");
    textlog = u"\t".join([timelog, action, text]);
    myLogger.info(textlog);
    
#------------------
# resources files
#------------------
@app.route('/_files/fonts/<filename>')
def send_image(filename):
    return static_file(filename, root = os.path.join(WEB_PATH,'web/resources/files/fonts'))
@app.route('/_files/xzero-rtl/css/<filename>')
def send_image(filename):
    return static_file(filename, root = os.path.join(WEB_PATH,'./web/resources/files/xzero-rtl/css'))

@app.route('/_files/xzero-rtl/js/<filename>')
def send_image(filename):
    return static_file(filename, root = os.path.join(WEB_PATH,'web/resources/files/xzero-rtl/js'))
@app.route('/_files/xzero-rtl/fonts/<filename>')
def send_image(filename):
    return static_file(filename, root = os.path.join(WEB_PATH,'web/resources/files/xzero-rtl/fonts'))


@app.route('/_files/samples/<filename:re:.*\.(png|jpg|jpeg)>')
def send_image(filename):
    return static_file(filename, root = os.path.join(WEB_PATH,'web/resources/files/samples'), mimetype='image/png')

@app.route('/_files/images/<filename:re:.*\.(png|jpg|jpeg)>')
def send_image(filename):
    return static_file(filename, root= os.path.join(WEB_PATH,'web/resources/files/images'), mimetype='image/png')
@app.route('/_files/<filename>')
def send_image(filename):
    return static_file(filename, root = os.path.join(WEB_PATH,'web/resources/files'))


@app.route('/')
@app.route('/main')
@app.route('/index')
#~ @view(os.path.join(WEB_PATH,'views/main2'))
@view('main2')
def main():
    #~ selection ="<textarea>Taha Zerrouki</textarea>"
    return {'DefaultText':u"جائحة كورونا",
      #~ 'ResultText':u"السلام عليكم",
      'ResultText':WEB_PATH,
      #~ 'Script':"cgi-bin/yaziji.cgi",
      'Script':".",
      #~ "Selection":selection
      }

@app.route('/ajaxGet')
#~ @app.route('/mishkal/ajaxGet')
#~ @view('main2')
def ajaxget():
    """
    this is an example of using ajax/json
    to test it visit http://localhost:8080/ajaxGet"
    """    
    text = request.query.text or u"تجربة"
    action = request.query.action or 'DoNothing'
    order = request.query.order or '0'

    options = dict(request.query.decode())

    if sys.version_info[0] < 3:
       options['lastmark']  = options.get('lastmark',"")#.decode('utf8')
       #~ pass

    writelog(text,action);
        #Handle contribute cases
    if action=="Contribute":
        return {'result':u"شكرا جزيلا على مساهمتك."}
    resulttext = adaat.DoAction(text ,action, options)
    
    #-----------
    # prepare json
    #-------------
    response.set_header("Access-Control-Allow-Methods",     "GET, POST, OPTIONS")
    response.set_header("Access-Control-Allow-Credentials", "true")
    response.set_header( "Access-Control-Allow-Origin",      "*")
    response.set_header("Access-Control-Allow-Headers",     "Content-Type, *")
    response.set_header( "Content-Type", "application/json")
    
    return json.dumps({'result':resulttext, 'order':order})




#------------------
# Static pages files
#------------------

@app.route('/mishkal/<filename>')
def server_static(filename):
    if filename in ("doc", "projects", "contact", "download","index"):
        return static_file(filename+".html", root= os.path.join(WEB_PATH,'web/resources/templates/'))
    else:
        return "<h2>Page Not found</h2>"

#------------------
# actions files
#------------------

@app.route('/<action>/<data>')            # matches /follow/defnull
def user_api(action, data):
    return "action %s, data %s"%(action, data)
from bottle import error

#------------------
# Error Pages
#------------------

@app.error(404)
def error404(error):
    return 'Nothing here, sorry' 
if __name__ == '__main__':
    try:
        run(app, host='localhost', port=8080, debug=True)
    except:
        run(app, host='127.0.0.1', port=8081, debug=True)        


