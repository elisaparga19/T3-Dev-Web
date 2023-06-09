#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgitb
import sys
from db import DB
from tools import *

cgitb.enable()
print("Content-type: text/html; charset=UTF-8")
sys.stdout.reconfigure(encoding='utf-8')
print()

#database = DB('localhost', 'root', '', 'tarea2')
database = DB('localhost', 'cc500242_u', 'ecpellente', 'cc500242_db')

name = 'Agregar Encargo'
title = 'AGREGAR ENCARGO'
inicio_form = f"""
                <form id="agregarEncargo" action="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/validar_encargo.py" method="POST" enctype="multipart/form-data">
                    <div class="form-row">
                        <div class="form-group">
                            {generate_description(False)}
                        </div>
                    </div>
                """
paises = generate_option_list(database, 'pais', 1)
ciudades = generate_option_list(database, 'ciudad', 1)
espacio = generate_option_list(database, 'espacio_encargo', 1)
kilos = generate_option_list(database, 'kilos_encargo', 1)
email = generate_email_input(False)
celular = generate_phone_input(False)
foto = """
        <div class="form-group" id="foto-encargo">
            <label>Foto encargo</label>
            <input type="file" class="form-control-file" name="foto-encargo-1">
        </div>
        <div id="errorFoto" style="color: red;" class="mb-4"></div>
        <button onclick="addInputFile()" type="button" class="btn mb-4">Agregar Foto</button>
"""

with open('../templates/template_agregar.html', 'r', encoding='utf-8') as template:
    file = template.read()
    print(file.format(name, title, inicio_form, paises, ciudades, paises, ciudades, "", espacio, kilos, email, celular, foto, ""))