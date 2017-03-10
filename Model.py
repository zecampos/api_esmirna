
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
import datetime


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'ze-api',
    'host': 'mongodb://jose:jose212121@ds161028.mlab.com:61028/ze-api'
}
db = MongoEngine(app)

class Membros(db.Document):
    Nome = db.StringField(max_length=200)
    DataNascimento = db.StringField(max_length=200)
    EstadoCivil = db.StringField(max_length=200)
    Sexo = db.StringField(max_length=200)
    Telefone = db.IntField()
    Rua = db.StringField(max_length=200)
    Numero = db.IntField()
    Complemento = db.StringField(max_length=200)
    Bairro = db.StringField(max_length=200)
    Cidade = db.StringField(max_length=200)
    Batizado = db.StringField(max_length=200)
    AnoBatismo = db.IntField()
    Discipulador = db.StringField(max_length=200)
    Celula = db.IntField()
    datacriacao = db.DateTimeField(default=datetime.datetime.now)

if __name__=='__main__':
    m = Membros()
    m.Nome = "Jose "
    m.DataNascimento = "08/09/1985"
    m.EstadoCivil = "casado"
    m.Sexo = "Masculino"
   
    m.save()

    print "Membros cadastrado com sucesso"