from peewee import *

db = SqliteDatabase('new.db')


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    uid = IntegerField()
    phone = IntegerField()
    username = TextField()
    first_name = TextField()
    last_name = TextField()
    tickets = IntegerField()


class Tickets(BaseModel):
    uid = IntegerField(unique=True)
    date = DateTimeField()
    amount = IntegerField()
    value = FloatField()
    user = ForeignKeyField(Users)
