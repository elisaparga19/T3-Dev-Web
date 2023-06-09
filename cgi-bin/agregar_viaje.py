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

name = 'Agregar Viaje'
title = 'AGREGAR VIAJE'
inicio_form = """<form id="agregarViaje" action="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/validar_viaje.py" method="POST" enctype="multipart/form-data">"""
paises = generate_option_list(database, 'pais', 1)
ciudades = generate_option_list(database, 'ciudad', 1)
email = generate_email_input(False)
celular = generate_phone_input(False)
fechas = """
                <div class="form-row">
                    <div class="col-auto form-group">
                        <label for="fecha-ida">Fecha ida</label>
                        <input class="form-control" type="text" id="fecha-ida" name="fecha-ida" placeholder="aaaa-mm-dd">
                    </div>
                    <div class="col-auto form-group">
                        <label for="fecha-regreso">Fecha regreso</label>
                        <input class="form-control" type="text" id="fecha-regreso" name="fecha-regreso" placeholder="aaaa-mm-dd">
                    </div>
                </div>
"""
espacio = generate_option_list(database, 'espacio_encargo', 1)
kilos = generate_option_list(database, 'kilos_encargo', 1)

with open('../templates/template_agregar.html', 'r', encoding='utf-8') as template:
    file = template.read()
    print(file.format(name, title, inicio_form, paises, ciudades, paises, ciudades, fechas, espacio, kilos, email, celular, "", ""))