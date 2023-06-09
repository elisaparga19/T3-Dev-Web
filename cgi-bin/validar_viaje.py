#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi 
import cgitb
import sys
from tools import *
from db import DB

cgitb.enable()
print("Content-type: text/html; charset=UTF-8")
sys.stdout.reconfigure(encoding='utf-8')
print()

name = 'Agregar Viaje'
title = 'AGREGAR VIAJE'
inicio_form = """<form id="agregarViaje" action="https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3/cgi-bin/validar_viaje.py" method="POST" enctype="multipart/form-data">"""

form = cgi.FieldStorage()

pais_origen = form.getvalue("pais-origen")
ciudad_origen = form.getvalue("ciudad-origen")
pais_destino = form.getvalue("pais-destino")
ciudad_destino = form.getvalue("ciudad-destino")
fecha_ida = form.getvalue("fecha-ida")
fecha_regreso = form.getvalue("fecha-regreso")
espacio_disponible = form.getvalue("espacio-disponible")
kilos_disponible = form.getvalue("kilos-disponibles")
email = form.getvalue("email")
celular = form.getvalue("celular")

#database = DB('localhost', 'root', '', 'tarea2')
database = DB('localhost', 'cc500242_u', 'ecpellente', 'cc500242_db')

p_origen = generate_option_list(database, 'pais', 1, pais_origen, True)
p_destino = generate_option_list(database, 'pais', 1, pais_destino, True)
c_origen = generate_option_list(database, 'ciudad', 1, ciudad_origen, True)
c_destino = generate_option_list(database, 'ciudad', 1, ciudad_destino, True)
espacio = generate_option_list(database, 'espacio_encargo', 1, espacio_disponible, True)
kilos = generate_option_list(database, 'kilos_encargo', 1, kilos_disponible, True)
fechas = generate_fechas(fecha_ida, fecha_regreso)
email_input = generate_email_input(email)
celular_input = generate_phone_input(celular)

error = ""
if pais_origen == "Elija un país...":
    error +=  "<p> Debe seleccionar un país de origen</p>"
if ciudad_origen == "Elija una ciudad...":
    error +=  "<p> Debe seleccionar una ciudad de origen</p>"
elif not check_city_country(database, pais_origen, ciudad_origen):
    error += "<p> Ciudad de origen no corresponde al país de origen seleccionado</p>"
if pais_destino == "Elija un país...":
    error += "<p> Debe seleccionar un país destino</p>"
if ciudad_destino == "Elija una ciudad...":
    error += "<p> Debe seleccionar una ciudad destino</p>"
elif not check_city_country(database, pais_destino, ciudad_destino):
    error += "<p> Ciudad de destino no corresponde al país de destino seleccionado</p>"
elif pais_origen == pais_destino:
    error += "<p>El pais de origen debe ser diferente al pais de destino</p>"
if not fecha_ida or not fecha_regreso:
    error += "<p>Debe ingresar fechas</p>"
elif not validate_dates(fecha_ida) or not validate_dates(fecha_regreso):
    error += "<p>Las fechas deben estar en formato aaaa-mm-dd</p>"
elif not compare_dates(fecha_ida, fecha_regreso):
    error += "<p>La fecha de regreso debe ser posterior a la fecha de ida</p>"
if espacio_disponible == "Seleccione espacio":
    error += "<p>Debe seleccionar un espacio</p>"
if kilos_disponible == "Seleccione peso":
    error += "<p>Debe seleccionar los kilos</p>"
if celular:
    if not check_phone_number(celular):
        error += '<p>Ingrese un número de celular válido </p>'
if not email:
    error += '<p> Ingrese un email </p>'
elif not check_email(email):
    error += '<p> Ingrese un email válido </p>'
if error == '':
    correct = """
    <div class="row justify-content-center vw-100" style="padding: 40px;">
        <div class="alert alert-success col-6" role="alert">
            <h4 class="alert-heading">Viaje ingresado con éxito!</h4>
            <p>¡Muchas gracias por su participación!</p>
            <hr>
        </div>
    </div>"""
    viaje = (database.get_id_from_name('ciudad', ciudad_origen), database.get_id_from_name('ciudad', ciudad_destino), fecha_ida, fecha_regreso, \
        database.get_id_from_value('kilos_encargo', kilos_disponible), database.get_id_from_value('espacio_encargo', espacio_disponible), email, celular)
    with open('../templates/template_index.html', 'r', encoding='utf-8') as template:
        file = template.read()
        database.agregar_viaje(viaje)
        print(file.format(correct))
else:
    with open('../templates/template_agregar.html', 'r', encoding='utf-8') as template:
        file = template.read()
        print(file.format(name, title, inicio_form, p_origen, c_origen, p_destino, c_destino, fechas, espacio, kilos, email_input, celular_input, "", error))
