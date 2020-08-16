import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# set FLASK_APP=api.py
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABSE_URI"] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# @app.route('/main_regions',methods=['GET'])
# def get_main_region_data:
#     all_main_regions=Main_regions.query.all()
# class Main_regions(Resource):
#     def get(self):
#         return {"data": "ok"}


# api.add_ressource(Main_regions,"/main_regions")

if __name__ == "__main__":
    app.run(debug=True)
