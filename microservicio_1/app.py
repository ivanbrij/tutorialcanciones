from microservicio_1 import create_app
from flask_restful import Resource, Api
from flask import Flask, request
import requests
import json
from celery import Celery

celery_app = Celery('task', broker='redis://localhost:6379/0')

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

@celery_app.task(name="tabla.registrar")
def registrar_puntaje(cancion_json):
    pass


class VistaPuntaje(Resource):
    def post(self, id_cancion):
        content = requests.get('http://127.0.0.1:5000/cancion/{}'.format(id_cancion))
        if content.status_code == 404:
            return content.json(),404
        else:
            cancion = content.json()
            cancion['puntaje'] = request.json['puntaje']
            args = (cancion,)
            registrar_puntaje.apply_async(args)
            return json.dumps(cancion)

api.add_resource(VistaPuntaje, '/cancion/<int:id_cancion>/puntuar')
