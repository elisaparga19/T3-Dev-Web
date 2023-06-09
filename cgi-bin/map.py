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
    result = db.get_last_five('viaje')
    print(json.dumps(result, default=str))

if info == 'encargo':
    result = db.get_last_five('encargo')
    print(json.dumps(result, default=str))

if info == 'origen':
    id = form.getvalue('id')
    ciudad = db.get_data_from_id('ciudad', id)[1]
    print(json.dumps(ciudad, default=str))

if info == 'destino':
    id = form.getvalue('id')
    ciudad = db.get_data_from_id('ciudad', id)[1]
    print(json.dumps(ciudad, default=str))