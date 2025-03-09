import os
from flask import Flask, request
from flask_restful import Resource, Api
from app_src.models import db, CustomerDetails, Service, ServiceCategory, Servicer, ServiceRequest, Feedback
from datetime import datetime
from app_src.api_1 import homePageAPI, adminLogin, customerLogin, customerSignUp, adminDashboard
from flask_jwt_extended import JWTManager
from datetime import timedelta



base_directory = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(base_directory,"urbanServices.sqlite3")
app.config["SECRET_KEY"] = "RSR_APP"
app.config["JWT_SECRET_KEY"] = "RSR"
app.config["JWT_ACCESS_TOKEN_EXPIRES"]=timedelta(hours=24)


db.init_app(app)
app.app_context().push()
api = Api(app)
jwt = JWTManager(app)


api.add_resource(homePageAPI, '/api/welcome')
api.add_resource(customerSignUp, '/customerSignUp')
api.add_resource(customerLogin, '/customerLogin')
api.add_resource(adminLogin, '/adminLogin')
api.add_resource(adminDashboard, '/adminDashboard')





@app.route('/')
def home():
    """new = ServiceCategory(sCat_id='cat_3', ser_desc='Electricals', created_date=datetime.now())
    db.session.add(new)
    db.session.commit()"""
    print(ServiceCategory.query.filter_by(sCat_id='cat_1').first())
    return {"hello":"me"}

class Home():
    def get(self):
        return {"api_stat":"from_class"}, 200
    def post(self):
        return {"post":"posts"},200
home_apis = Home()
@app.route('/api', methods=["GET", "POST"])
def new_route():
    if request.method=="GET":
        return home_apis.get()
    elif request.method == "POST":
        return home_apis.post()
class newHome():
    def get(self):
        return {"new":"home_api"}
newHome_api = newHome()
@app.route('/api/class')
def new_route_1():
    return newHome_api.get()



if __name__ == "__main__":
    db.create_all()
    app.run()