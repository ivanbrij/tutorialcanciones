from flaskr import create_app
from .modelos import db, Cancion

app = create_app('default')
app_context = app.app_context()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial_canciones.db'
app.config['SQLALCHEMY_MODIFICATIONS'] = False
app_context.push()

db.init_app(app)
db.create_all()

#Prueba
with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=25, interprete='Jorge Barrera')
    c2 = Cancion(titulo='Prueba2', minutos=2, segundos=25, interprete='Jorge Barrera')
    db.session.add(c)
    db.session.add(c2)
    db.session.commit()
    print(Cancion.query.all())
