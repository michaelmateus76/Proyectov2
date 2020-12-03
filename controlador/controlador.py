import sys  
sys.path.append('/usr/lib/cgi-bin/proyecto/modelo')

import json
from actividad import actividadClass as mod
from flask import Flask,Response,request

app = Flask(__name__)

@app.route('/cargarActividad',methods=['GET'])
def consultarActividades():
        actividades = mod.obtenerActividades()
        return Response(json.dumps(actividades),  mimetype='application/json')

@app.route('/agregarCronograma',methods=['POST'])
def addCro():
        nombreAct= request.form.get("nombreAct").encode('utf-8')
        nombreMat= request.form.get("nombreMat").encode('utf-8')
        hora= request.form.get("hora").encode('utf-8')
        fecha= request.form.get("fecha").encode('utf-8')
        mod.agregarCrono(nombreAct,nombreMat,hora,fecha)
        return "true"

@app.route('/cargarCronograma',methods=['POST'])
def viewCro():
        fecha= request.form.get("fecha").encode('utf-8')
        cronograma = mod.cargarCrono(fecha)
        return Response(json.dumps(cronograma),  mimetype='application/json')
        
@app.route('/deleteCronograma',methods=['POST'])
def deleteCro():
        nombre= request.form.get("nombre").encode('utf-8')
        mod.deleteCrono(nombre)
        return "true"


if __name__ == '__main__':
        app.run(host='0.0.0.0')
