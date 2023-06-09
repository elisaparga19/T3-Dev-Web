#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import cgi 
import json
from db import DB

print('Access-Control-Allow-Origin: *')
print("Content-type:  application/json; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

#db = DB('localhost', 'root', '', 'tarea2')
db = DB('localhost', 'cc500242_u', 'ecpellente', 'cc500242_db')

form = cgi.FieldStorage()
info = form.getvalue('info')

if info == 'viaje':
    result = db.get_data('viaje')
    print(json.dumps(result, default=str))

if info == 'encargo':
    result = db.get_data('encargo')
    print(json.dumps(result, default=str))

if info == 'espacio':
    result = db.get_data('espacio_encargo')
    print(json.dumps(result, default=str))

if info == 'kilos':
    result = db.get_data('kilos_encargo')
    print(json.dumps(result, default=str))
