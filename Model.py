
from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'ze-api',
    'host': 'mongodb://jose:jose212121@ds161028.mlab.com:61028/ze-api'
}
db = MongoEngine(app)
print (db)