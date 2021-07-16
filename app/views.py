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
    food_instance.save()
    return food_instance.to_json(), 201


@app.route('/all')
def show_all():
    pass
