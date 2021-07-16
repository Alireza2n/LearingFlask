import mongoengine as me


class Food(me.Document):
    name = me.StringField(required=True)
    region = me.ListField()
    description = me.StringField()
    image = me.ImageField()
