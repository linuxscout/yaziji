#!/usr/bin/python3
# -*- coding=UTF-8 -*-
import sys, os, os.path, re
import os;
import locale; 
os.environ["PYTHONIOENCODING"] = "utf-8"; 
from glob import glob
sys.path.append('yaziji/web/');
sys.path.append('yaziji');
sys.path.append('yaziji/yaziji');
from bottle import run
import testy

if __name__ == '__main__':
    run(testy.app, host='localhost', port=8080, debug=True, server="cgi")    
