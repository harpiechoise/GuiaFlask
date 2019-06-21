from flask import Flask, render_template, request
import json
from dbFuncs import simpleUser

app = Flask('__name__') #Instacia de flask con el nombre del archivo actual

@app.route('/') #Seteamos la ruta al index
def index():
    return render_template('index.html') #Le mandamos el index.html que ahora voy a crear

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    usuario = request.form['usr'] #Leer el usuario del request
    contraseña = request.form['pwd'] #Leer la contraseña 
    try:
        #Intentar agregar el usuario
        simpleUser.addUser(usuario, contraseña) #agregar el usuario
        return json.dumps({'Status':'OK'}) #Si sale bien enviar una señal de ok a jQuery 
    except:
        return json.dumps({'Status':'ERR'}) #En el caso contrario enviar un error

@app.route('/iniciar', methods=['GET', 'POST'])
def iniciar():
    usuario = request.form['usr']
    contraseña = request.form['pwd']
    try:
        simpleUser.iniciarSesion(usuario, contraseña)
        return json.dumps({'Status':'OK'})
    except:
        return json.dumps({'Status':'ERR'})
    
if __name__ == '__main__':
    app.run(port=8081, debug=True)

    #Perdon XD, me perdi cuadno entraste a los template
    #No se sobre eso 
    #Pero tratare de entenderlo, bye
    #OK