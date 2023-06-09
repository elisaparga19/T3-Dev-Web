#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import mysql.connector
import sys

class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def agregar_viaje(self, data):
        try:
            sql =f'''
                INSERT INTO viaje (origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero)
                VALUES ({data[0]}, {data[1]}, '{data[2]}', '{data[3]}', {data[4]}, {data[5]}, '{data[6]}', '{data[7]}')
                '''
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print("ERROR AL GUARDAR VIAJE EN LA BASE DE DATOS")
            sys.exit()

    def agregar_encargo(self, data):
        try:
            sql =f'''
                INSERT INTO encargo (descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador)
                VALUES ('{data[0]}', {data[1]}, {data[2]}, {data[3]}, {data[4]}, '{data[5]}', '{data[6]}');
                '''
            self.cursor.execute(sql)
            self.db.commit()
            encargo_id = self.cursor.lastrowid
            for foto in data[7]:
                self.agregar_foto('/media/', foto, encargo_id)
        except:
            print("ERROR AL GUARDAR ENCARGO EN LA BASE DE DATOS")
            sys.exit()

    def agregar_foto(self, path_foto, nombre_foto, encargo_id):
        try:
            sql = f'''INSERT INTO foto (ruta_archivo, nombre_archivo, encargo_id) VALUES ('{path_foto}', '{nombre_foto}', {encargo_id})'''
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print("ERROR AL GUARDAR ENCARGO EN LA BASE DE DATOS")
            sys.exit()

    def get_data(self, table):
        sql = f'''
            SELECT * FROM {table};
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_id_from_name(self, table, name):
        sql = " SELECT id FROM {} WHERE nombre='{}' ".format(table, name)
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def get_data_from_id(self, table, id):
        sql = " SELECT * FROM {} WHERE id={} ".format(table, id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_id_from_value(self, table, value):
        sql = " SELECT id FROM {} WHERE valor='{}' ".format(table, value)
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def get_city_from_country(self, country):
        country_id = self.get_id_from_name('pais', country)
        sql = f"SELECT nombre FROM ciudad WHERE pais={country_id}"
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]

    def get_five_rows_from_table(self, table, counter):
        sql = f'''SELECT * FROM {table} ORDER BY id ASC LIMIT {counter}, 5'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_last_five(self, table):
        sql = f'''SELECT * FROM {table} ORDER BY id DESC LIMIT 6'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_foto_from_encargo_id(self, encargo_id):
        sql = f'''SELECT * FROM foto WHERE encargo_id={encargo_id} LIMIT 1'''
        self.cursor.execute(sql)
        return self.cursor.fetchall()