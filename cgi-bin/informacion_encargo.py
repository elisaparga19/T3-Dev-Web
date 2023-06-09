#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from db import DB
from tools import *
import os

print("Content-type: text/html; charset=UTF-8")
sys.stdout.reconfigure(encoding='utf-8')
print()

#database = DB('localhost', 'root', '', 'tarea2')
database = DB('localhost', 'cc500242_u', 'ecpellente', 'cc500242_db')
query_string = os.environ.get('QUERY_STRING')
id = query_string.split("=")[1]
foto = f"""<img alt="Encargo {id}" src="{get_img_source(database, id)}" id="img" onclick="changeSize()" width="640" height="480">"""

data = database.get_data_from_id('encargo', id)


info_encargo = f"""<div class="container align-items-center justify-content-center">
                    <div class="d-flex">
                    <div class="flex-column">
                        <p id="descripcion">Descripción: {data[1]}</p>
                        <p id="espacio">El encargo presenta un volumen de: {database.get_data_from_id('espacio_encargo', data[2])[1]}</p>
                        <p id="kilos">El encargo pesa: {database.get_data_from_id('kilos_encargo', data[3])[1]}</p>
                        <p id="origen">Este encargo debe ser enviado desde: {generate_table_format(database, data[4])}</p>
                        <p id="destino">Este encargo debe llegar a: {generate_table_format(database, data[5])}</p>
                        <p id="email">Email de contacto: {data[6]}</p>
                        <p id="celular">Celular de contacto: {display_phone(data[7])}</p>
                        <p><a href="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/ver_encargos.py" style="color: #2e5181">Volver al listado de encargos</a></p>
                    </div>
                    <div class="flex-column">
                        <p id="foto" class="mb-4">Foto del encargo: {foto}</p>
                    </div>
                    </div>
                </div>"""

with open('../templates/template_informacion.html', 'r', encoding='utf-8') as template:
    file = template.read()
    print(file.format('Información Encargo', 'INFORMACIÓN ENCARGO', info_encargo))