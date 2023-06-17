#!/usr/bin/env python3
import sys
sys.path.insert(0,"/var/www/html/yaziji/webfrontend/")
sys.path.insert(0,"/var/www/html/yaziji/web/")
sys.path.insert(0,"/var/www/html/yaziji/")
sys.path.append("/var/www/html/yaziji/yaziji")
sys.path.append("/var/www/html/yaziji/web")
import os
os.environ["REQUEST_METHOD"] = "GET"; 

# ~ import os
# ~ # Change working directory so relative paths (and template lookup) work again
# ~ os.chdir(os.path.dirname(__file__))


# ~ from testylang import wsgi_app  as application
from yaziji_webserver import app  as application
# just for testing
def application2(environ,start_response):
    status = '200 OK'
    html = '<html>\n' \
           '<body>\n' \
           '<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n' \
           'Welcome to mod_wsgi Test Page\n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n'
    html = bytes(html, encoding= 'utf-8')           
    response_header = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(html)))]

    start_response(status,response_header)
    
    return [html]

