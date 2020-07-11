import sys
from bottle import Bottle, run
from bottle import static_file
from bottle import template
from bottle import view
from bottle import get
from bottle import request
from bottle import response

import json
import os.path
sys.path.append(os.path.join("/home/zerrouki/workspace/projects/mishkal-project/mishkal-2017-03-19/"))
import adaat
app = Bottle()


#------------------
# resources files
#------------------
@app.route('/_files/fonts/<filename>')
def send_image(filename):
    return static_file(filename, root='./web/resources/files/fonts')
@app.route('/_files/xzero-rtl/css/<filename>')
def send_image(filename):
    return static_file(filename, root='./web/resources/files/xzero-rtl/css')

@app.route('/_files/xzero-rtl/js/<filename>')
def send_image(filename):
    return static_file(filename, root='./web/resources/files/xzero-rtl/js')
@app.route('/_files/xzero-rtl/fonts/<filename>')
def send_image(filename):
    return static_file(filename, root='./web/resources/files/xzero-rtl/fonts')


@app.route('/_files/samples/<filename:re:.*\.(png|jpg|jpeg)>')
def send_image(filename):
    return static_file(filename, root='./web/resources/files/samples', mimetype='image/png')

@app.route('/_files/images/<filename:re:.*\.(png|jpg|jpeg)>')
def send_image(filename):
    return static_file(filename, root='./web/resources/files/images', mimetype='image/png')
@app.route('/_files/<filename>')
def send_image(filename):
    return static_file(filename, root='./web/resources/files')





@app.route('/mishkal/main')
@app.route('/mishkal/index')
@view('main2')
def main():
    #~ selection ="<textarea>Taha Zerrouki</textarea>"
    return {'DefaultText':u"جائحة كورونا",
      'ResultText':u"السلام عليكم",
      #~ "Selection":selection
      }

@app.route('/ajaxGet')
@app.route('/mishkal/ajaxGet')
#~ @view('main2')
def ajaxget():
    """
    this is an example of using ajax/json
    to test it visit http://localhost:8080/ajaxGet"
    """    
    text = request.query.text or u"تجربة"
    action = request.query.action or 'DoNothing'
    order = request.query.order or '0'
    #options = {};
    #options['lastmark'] = request.query.lastmark or '1'

    #options['subject'] = request.query["options[subject]"] or ''
    #options['object'] = request.query["options[object]"] or ''
    #options['verb'] = request.query["options[verb]"] or ''
    #options['time'] = request.query["options[time]"] or ''
    #options['place'] = request.query["options[place]"] or ''
    options = dict(request.query.decode())
    #print("Options", options)
    if sys.version_info[0] < 3:
       text = text.decode('utf-8')
       options['lastmark']  = options['lastmark'].decode('utf8')

    #self.writelog(text,action);
        #Handle contribute cases
    if action=="Contribute":
        return {'result':u"شكرا جزيلا على مساهمتك."}
    resulttext = adaat.DoAction(text ,action, options)
    #~ resulttext = u"تم إنجاز المهمة بنجاح"
    
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
        return static_file(filename+".html", root='./web/resources/templates/')
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
run(app, host='localhost', port=8080, debug=True)


