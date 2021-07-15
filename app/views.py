from flask_pymongo import PyMongo

from . import app

# Connection String
# mongodb://myDBReader:D1fficultP%40ssw0rd@mongodb0.example.com:27017/?authSource=admin
app.config["MONGO_URI"] = 'mongodb://root:123456@localhost:27017/maktab?authSource=admin'
mongo = PyMongo(app)



@app.route('/')
def index():
    return 'Index'


@app.route('/all')
def show_all():
    all_docs = mongo.db.flask.find()
    return all_docs[0]
