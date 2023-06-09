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

data = database.get_data_from_id('viaje', id)

info_viaje = f"""<div class="container">
                    <p id="origen">Este viaje tiene como origen: {generate_table_format(database, data[1])}</p>
                    <p id="destino">Este viaje tiene como destino: {generate_table_format(database, data[2])}</p>
                    <p id="fecha-ida">La fecha de ida es el día: {change_date_format(data[3])}</p>
                    <p id="fecha-regreso">La fecha de regreso es el día: {change_date_format(data[4])}</p>
                    <p id="espacio">Este viaje tiene como disponibilidad un volumen de: {database.get_data_from_id('espacio_encargo', data[6])[1]}</p>
                    <p id="kilos">El peso disponible es de: {database.get_data_from_id('kilos_encargo', data[5])[1]}</p>
                    <p id="email">Email de contacto del viajero: {data[7]}</p>
                    <p id="celular">Celular de contacto del viajero: {display_phone(data[8])}</p>
                    <p><a href="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/ver_viajes.py" style="color: #2e5181">Volver al listado de viajes</a></p>
                </div>"""

with open('../templates/template_informacion.html', 'r', encoding='utf-8') as template:
    file = template.read()
    print(file.format('Información Viaje', 'INFORMACIÓN VIAJE', info_viaje))