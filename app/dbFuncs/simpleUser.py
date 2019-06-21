# -*- coding: utf-8 -*-
import hashlib
import pprint
from dbFuncs.cn import connect
def encriptarContraseña(contraseña):
    #Voy a hacer una autentificacion simple
    md = hashlib.md5() #Instanciado md5
    md.update(contraseña.encode('utf-8')) #Añadir contraseña
    return md.digest() #Encriptado md5
    #Esto lo entiendo un poco, se que es lo de hashing para incriptar y
    #Supongo que el md5, es el ultimo de esa serie
    #La verdad eso lo he investigado poco, lo escuche en una feria de la escueal


def addUser(usuario, contraseña):
    contraseñaEnc = encriptarContraseña(contraseña)
    Tabla = conection.connect()
    query = {'user':usuario, 'pass':contraseñaEnc}
    id = Tabla.insert_one(query)
    
    #He visto lo de las primeras lineas 1-2, ¿Para que son?
    #Para que el codigo se interprete como UTF-8 y no ASCII
   
    #¿Para que se utiliza pprint?
    #Significa Pretty Print y es para formatear un poco cuando mostramos por consolas diccionarios o arrays grandes 
    #Revisa el codigo, y hasme algunas preguntas yo voy y vuelv
    #Ejecuta codigo si quieres, juega con las funciones, has lo que quieras, asi se aprende
    #Aun estoy ocupado pero creare la estructura de carpetas para que no te aburras

def findAll():
    Tabla = conection.connect()
    query = {}
    for documment in Tabla.find(query):
        print(documment)


def iniciarSesion(usuario, contraseña):
    Tabla = conection.connect() #Llamamos a la tabla
    query = {'user':usuario}    #Enviamos la query con el usuario
    contraseñaEnc = Tabla.find_one(query)['pass'] #Tomamos la contraseña encriptada
    if contraseñaEnc == encriptarContraseña(contraseña): #Encriptamos la contraseña recivida y la comparamos con la contraseña encriptada
        print('Sesion iniciada') #Si son iguales iniciamos sesion
    else: 
        print('La contraseña es incorrecta') #De otro modo la contraseña es incorecta
if __name__ == '__main__': #Definir que cuando se ejecute este archivo se hara un entorno de prueba
    addUser('Jose', 'Alv')
    #Asi se hace un inicio de sesion seguro en la base de datos 
    iniciarSesion('Jose', 'Alv')

    #Entienddo el codigo 
    #Ya que es conexion, buscas el registro dependiendo el usuario, y la contrase;a encriptada
    #Lo de coneccion a mongo fue como lo mas extra;o, porque no lo habia visto 
    #Y lo de JSON, nunca he trabajado con JSON
    #JSON es lo mas importante para todo esto de la web, soluciona todos los problemas de mover datos de un lado a otro
    #Dehecho ahora para hacer un registro de usuario y un inicio de sesion el flask usaremos json para comunicar la api con la pagina
    #Asi evitamos recargar usando javascript prevent default, y parecera mas natural todo, ahi veras