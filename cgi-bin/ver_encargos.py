#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgitb
import sys
from db import DB
from tools import *
import os

cgitb.enable()
print("Content-type: text/html; charset=UTF-8")
sys.stdout.reconfigure(encoding='utf-8')
print()

query_string = os.environ.get('QUERY_STRING')

counter = control_counter(query_string)

#database = DB('localhost', 'root', '', 'tarea2')
database = DB('localhost', 'cc500242_u', 'ecpellente', 'cc500242_db')
foto = """<th id="foto" scope="col">Foto</th>"""

nav_bar = f"""<nav>
                <ul class="pagination">
                    <li class="page-item {disable_previous(counter)}"><a class="page-link" href="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/ver_encargos.py?action=previous&counter={counter}">Previous</a></li>
                    <li class="page-item {disable_next(database, 'encargo', counter)}"><a class="page-link" href="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/ver_encargos.py?action=next&counter={counter}">Next</a></li>
                </ul>
            </nav>"""

def generate_row_from_element(encargo):
    id = encargo[0]
    row = f"""
        <tr id={id} data-href="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/informacion_encargo.py?id={id}">
            <td>{generate_table_format(database, encargo[4])}</td>
            <td>{generate_table_format(database, encargo[5])}</td>
            <td>{database.get_data_from_id('espacio_encargo', encargo[2])[1]}</td>
            <td>{database.get_data_from_id('kilos_encargo', encargo[3])[1]}</td>
            <td>{encargo[6]}</td>
            <td><img alt="Encargo {id}" src="{get_img_source(database, id)}" width="120" height="120"></td>
        </tr>
    """
    return row

with open('../templates/template_ver.html', 'r', encoding='utf-8') as template:
    file = template.read()
    print(file.format('Ver Encargos', 'VER ENCARGOS', '', foto, generate_rows_to_display(database, 'encargo', counter, generate_row_from_element), nav_bar))