#!/usr/bin/env python3

import os
import sys

files = input("Ingrese el nombre de archivo:\n")
name = input("ingrese nombre de la aplicacion:\n")
comment = input("ingrese una descripcion de la aplicacion:\n")
exec = input("ingrese comando a ejecutar:\n")
icon = input("ingrese direccion de la imagen:\n")

file = open(files + ".desktop", "w")
file.write("[Desktop Entry]" + os.linesep)
file.write("Encoding=UTF-8" + os.linesep)
file.write("Version=1.0" + os.linesep)
file.write("Name=" + name.capitalize() + os.linesep)
file.write("Comment=" + comment.capitalize() + os.linesep)
file.write("Exec=" + exec + os.linesep)
file.write("Icon=" + icon + os.linesep)
file.write("Type=Application" + os.linesep)

def mostrar_menu(opciones):
    print('Seleccione un item:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, salida):
    opcion = None
    while opcion != salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

print("Elige si quieres que la terminal se ejecute:\n")
def menu1():
    opciones = {
        '1': ('Si', true),
        '2': ('No', false),
        '3': ('Salir', salir)
    }
    generar_menu(opciones, '3')

def true():
    file.write("Terminal=True" + os.linesep)

def false():
    file.write("Terminal=False" + os.linesep)

def salir():
    print('Saliendo')

def menu():
    opciones = {
        '01': ('Sonido y video', AudioVideo),
        '02': ('Programacion', Development),
        '03': ('Educacion y ciencias', Education),
        '04': ('Juegos', Game),
        '05': ('Graficos', Graphics),
        '06': ('Internet', Network),
        '07': ('Oficina', Office),
        '08': ('Preferencias', Settings),
        '09': ('herramientas del sistema', System),
        '10': ('Accesorios', Utility),
        '11': ('Salir', salir)
    }
    generar_menu(opciones, '11')

def AudioVideo():
    file.write("Categories=AudioVideo" + ";")

def Development():
    file.write("Categories=Development" + ";")

def Education():
    file.write("Categories=Education" + ";")

def Game():
    file.write("Categories=Game" + ";")

def Graphics():
    file.write("Categories=Graphics" + ";")

def Network():
    file.write("Categories=Network" + ";")

def Office():
    file.write("Categories=Office" + ";")

def Settings():
    file.write("Categories=Settings" + ";")

def System():
    file.write("Categories=System" + ";")

def Utility():
    file.write("Categories=Utility" + ";")

def salir():
    print('Saliendo')

menu1()
menu()

file.close()
