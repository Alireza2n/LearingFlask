from werkzeug.exceptions import abort

from . import app
from . import models


@app.route('/')
def index():
    return 'Index'


@app.route('/food/create')
def create_food():
    food_instance = models.Food(
        name='قلیه ماهی',
        description='ماهی با سبزیجات و ترشی انبه'
    )
    food_instance.region = ['بندرعباس', 'هرمز']
    food_instance.image = open('/home/alireza/Projects/MaktabFlask/app/mahi.jpeg', 'rb')
    food_instance.save()
    return food_instance.to_json(), 201


@app.route('/food')
def get_food():
    food_instance = models.Food.objects(name='پیتزا').first()
    if food_instance is None:
        abort(404)
    return food_instance.to_json()


@app.route('/all')
def show_all():
    food_instance = models.Food.objects.all()
    if food_instance is None:
        abort(404)
    return food_instance.to_json()
