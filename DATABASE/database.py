from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, MetaData, Sequence, create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
metadata = MetaData()
import pandas as pd
from DATA.data import main_regions, secondary_regions, all_abbayes, abbaye_data_list_text

app = Flask(__name__)

db = SQLAlchemy(app)
df = pd.DataFrame([main_regions])
df2 = pd.DataFrame([secondary_regions])
df3 = pd.DataFrame([all_abbayes])
df4 = pd.DataFrame([abbaye_data_list_text])

users = Table('users', metadata,
              Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
              Column('name', String(50)),
              Column('fullname', String(50)),
              Column('nickname', String(50))
              )
inserstion_of_user = users.insert().values(name='BOURY', fullname='Alex BOURY', nickname='Sancty')

metadata.create_all(engine)
class User(db.Model):
    username = db.Column(db.String(80), unique=True)
    pw_hash = db.Column(db.String(80))


class Main_regions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    secondary_region_id = db.Column(db.Integer, db.ForeignKey('secondary_region.id'), nullable=False)

    def __init__(self, name):
        self.id = id
        self.name = name


class Secondary_regions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)

    def __init__(self, name):
        self.id = id
        self.name = name
