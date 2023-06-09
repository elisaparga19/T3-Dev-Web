#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mimetypes
import os
import re
import datetime
from hashlib import sha512

regex_phone_number = "^\\+569\d{8}$"
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def generate_option_list(db, table_name, index, value="", selected=False):
    '''
    Generate option list with selected value if it exists
    '''
    table = db.get_data(table_name)
    options = ""
    for data in table:
        if selected and data[index] == value:
            options += f"""<option selected>{data[index]}</option>"""
        else:
            options += f"""<option>{data[index]}</option>"""
    return options

def check_city_country(db, pais, ciudad):
    '''
    Check that the selected city corresponds with selected country
    '''
    ciudad_pais = db.get_city_from_country(pais)
    return ciudad_pais == ciudad


def check_email(email):
    '''
    Check email format
    '''
    return (re.fullmatch(regex_email, email))

def check_phone_number(phone_number):
    '''
    Check phone number format
    '''
    return (re.fullmatch(regex_phone_number, phone_number))

def generate_email_input(email):
    '''
    Generate html with email with registered value if it exists
    '''
    if email:
        return f"""<input value={email} class="form-control" type="text" id="email" name="email" placeholder="aaaa@bbbb.com" size="30">"""
    else:
        return """<input class="form-control" type="text" id="email" name="email" placeholder="aaaa@bbbb.com" size="30">"""

def generate_phone_input(phone_number):
    '''
    Generate html with phone number with registered value if it exists
    '''
    if phone_number:
        return f"""<input value={phone_number} class="form-control" type="text" id="celular" name="celular" placeholder="+56987654321" size="15">"""
    else:
        return """<input class="form-control" type="text" id="celular" name="celular" placeholder="+56987654321" size="15">"""

def generate_description(description):
    '''
    Generate html with description with registered description if it exists
    '''
    if description:
        return f"""<label for="descripcion">Descripción encargo</label>
                   <input value={description} class="form-control" size="100" id="descripcion" name="descripcion">"""
    else:
        return """<label for="descripcion">Descripción encargo</label>
                  <input class="form-control" size="100" id="descripcion" name="descripcion">"""

def generate_fechas(fecha_ida, fecha_regreso):
    '''
    Generate html with dates with registered values if they exist
    '''
    if fecha_ida:
        fecha_ida_html = f"""<div class="form-row">
                                <div class="col-auto form-group">
                                    <label for="fecha-ida">Fecha ida</label>
                                    <input value={fecha_ida} class="form-control" type="text" id="fecha-ida" name="fecha-ida" placeholder="aaaa-mm-dd">
                                </div> """
    else:
        fecha_ida_html = """<div class="form-row">
                                <div class="col-auto form-group">
                                    <label for="fecha-ida">Fecha ida</label>
                                    <input class="form-control" type="text" id="fecha-ida" name="fecha-ida" placeholder="aaaa-mm-dd">
                                </div>"""
    if fecha_regreso:
        fecha_regreso_html = f"""<div class="col-auto form-group">
                                    <label for="fecha-regreso">Fecha regreso</label>
                                    <input value={fecha_regreso} class="form-control" type="text" id="fecha-regreso" name="fecha-regreso" placeholder="aaaa-mm-dd">
                                </div>
                            </div>"""
    else:
        fecha_regreso_html = """<div class="col-auto form-group">
                                    <label for="fecha-regreso">Fecha regreso</label>
                                    <input class="form-control" type="text" id="fecha-regreso" name="fecha-regreso" placeholder="aaaa-mm-dd">
                                </div>
                            </div>"""
    return fecha_ida_html+fecha_regreso_html

def validate_dates(date):
    '''
    Check if the registered date is in the correct format
    '''
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def compare_dates(fecha_ida, fecha_regreso):
    '''
    Check if feche_regreso is after fecha_ida
    '''
    date_ida = datetime.datetime.strptime(fecha_ida, "%Y-%m-%d")
    date_regreso = datetime.datetime.strptime(fecha_regreso, "%Y-%m-%d")
    return date_regreso > date_ida

def generate_file_list(form):
    '''
    Returns a list of fileitems of images uploaded in the form
    '''
    file_list = []
    for i in range(1,4):
        name = 'foto-encargo-{}'.format(i)
        try:
            form[name]
            file_list.append(form[name])
        except:
            pass
    return file_list

def check_file_size_type(file_list):
    for file in file_list:
        try:
            size = os.fstat(file.file.fileno()).st_size #tamaño en bytes
            tipo_real = mimetypes.guess_type(file.filename)[0]
            if size >= 1000000:
                return '<p>Tamaño de la imagen muy grande</p>'
            if tipo_real not in ['image/jpeg', 'image/png']:
                return '<p>Ingrese una imagen en formato JPG, JPEG o PNG</p>'
            else:
                return ''
        except:
            return "<p>Error al obtener tamaño y tipo del archivo</p>"

def store_images(fileitems):
    '''
    Save images in media folder and returns a list containing the hash filenames
    '''
    filenames = []
    for fileitem in fileitems:
        filename = fileitem.filename
        hash_filename = sha512(filename.encode('utf-8')).hexdigest() + '.jpg'
        filenames.append(hash_filename)
        path = f'''../media/{hash_filename}'''
        with open(path, "wb") as save_file:
            save_file.write(fileitem.file.read())
    return filenames

def generate_table_format(database, city_id):
    '''Generate origin or destination to display in table ver_viajes/ver_encargos'''
    data_city = database.get_data_from_id('ciudad', city_id)
    city = data_city[1]
    country_id = data_city[2]
    data_country = database.get_data_from_id('pais', country_id)
    country = data_country[1]
    return f'''{city}, {country}'''

def change_date_format(date):
    return date.strftime("%Y-%m-%d")

def generate_rows_to_display(database, tabla, counter, row_generator):
    table_data = database.get_five_rows_from_table(tabla, counter)
    rows_to_display = ""
    for element in table_data:
        row = row_generator(element)
        rows_to_display += row
    return rows_to_display

def disable_next(database, table, current_counter):
    data = database.get_five_rows_from_table(table, current_counter+5)
    if data == []:
        return 'disabled'

def disable_previous(current_counter):
    if current_counter-5 < 0:
        return 'disabled'

def control_counter(query_string):
    if not query_string:
        counter = 0
    else:
        param_list = query_string.split('&')
        action = param_list[0].split('=')[1]
        counter = int(param_list[1].split('=')[1])
        if action == "next":
            counter += 5
        elif action == "previous" and counter >= 5:
            counter -= 5
    return counter

def display_phone(phone_number):
    if phone_number:
        return phone_number
    else:
        return "No especificado"

def get_img_source(database, encargo_id):
    foto = database.get_foto_from_encargo_id(encargo_id)[0]
    ruta_archivo = foto[1]
    nombre_archivo = foto[2]
    return "https://anakena.dcc.uchile.cl/~cc500210/cgi-bin/tarea-3{}{}".format(ruta_archivo, nombre_archivo)
