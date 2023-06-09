#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgitb
import sys
from db import DB
import os
from tools import *


cgitb.enable()
print("Content-type: text/html; charset=UTF-8")
sys.stdout.reconfigure(encoding='utf-8')
print()

query_string = os.environ.get('QUERY_STRING')

counter = control_counter(query_string)

#database = DB('localhost', 'root', '', 'tarea2')
database = DB('localhost', 'cc500242_u', 'ecpellente', 'cc500242_db')
fechas = """
            <th id="fechaIda" scope="col">Fecha Ida</th>
            <th id="fechaRegreso" scope="col">Fecha Llegada</th>
        """

nav_bar = f"""<nav>
                <ul class="pagination">
                    <li class="page-item {disable_previous(counter)}"><a class="page-link" href="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/ver_viajes.py?action=previous&counter={counter}">Previous</a></li>
                    <li class="page-item {disable_next(database, 'viaje', counter)}"><a class="page-link" href="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/ver_viajes.py?action=next&counter={counter}">Next</a></li>
                </ul>
            </nav>"""

def generate_row_from_element(viaje):
    row = f"""
        <tr id={viaje[0]} data-href="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/informacion_viaje.py?id={viaje[0]}">
            <td>{generate_table_format(database, viaje[1])}</td>
            <td>{generate_table_format(database, viaje[2])}</td>
            <td>{change_date_format(viaje[3])}</td>
            <td>{change_date_format(viaje[4])}</td>
            <td>{database.get_data_from_id('espacio_encargo', viaje[6])[1]}</td>
            <td>{database.get_data_from_id('kilos_encargo', viaje[5])[1]}</td>
            <td>{viaje[7]}</td>
        </tr>
    """
    return row

with open('../templates/template_ver.html', 'r', encoding='utf-8') as template:
    file = template.read()
    print(file.format('Ver Viajes', 'VER VIAJES', fechas, '', generate_rows_to_display(database, 'viaje', counter, generate_row_from_element), nav_bar))