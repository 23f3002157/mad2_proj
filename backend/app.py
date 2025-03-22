import os, time
from flask import Flask, request
from flask_restful import Resource, Api
from app_src.models import db, CustomerDetails, Service, ServiceCategory, Servicer, ServiceRequest, Feedback
from datetime import datetime
from app_src.api_1 import homePageAPI, adminLogin, customerLogin, customerSignUp, adminDashboard, customerDashboard, adminNewService, adminCustomer, cache
from app_src.api_1 import servicerLogin, servicerSignUp, getServices, getCustomers, blockCustomerAdmin, getServicers, toggleServicerAdmin
from app_src.api_1 import getServicesAdmin, adminEditService, adminSearch, adminSummary, getCustomerDetails, getServiceRequest
from app_src.api_1 import getServicersCustomer, customerServiceRequest, deleteCustomerRequest, updateCustomerRequest, customerSearch
from app_src.api_1 import customerSummary, getServiceRequestsServicer, updateRequestServicer, closeServiceCutomer
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_caching import Cache
from app_src.worker import celery
from app_src.task import *
from flask_cors import CORS


base_directory = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+ os.path.join(base_directory,"urbanServices.sqlite3")
app.config["SECRET_KEY"] = "RSR_APP"
app.config["JWT_SECRET_KEY"] = "RSR"
app.config["JWT_ACCESS_TOKEN_EXPIRES"]=timedelta(hours=24)
app.config["CACHE_TYPE"] = 'redis'
app.config["CACHE_REDIS_HOST"] = "localhost"
app.config["CACHE_REDIS_PORT"] = 6379
app.config["CACHE_REDIS_DB"] = 0
app.config["CACHE_DEFAULT_TIMEOUT"] = 300
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379"
celery.conf.update(
    broker_url="redis://localhost:6379/0",
    result_backend = "redis://localhost:6379/0",
    timezone = "Asia/Kolkata"
)

CORS(app)
db.init_app(app)
api = Api(app)
jwt = JWTManager(app)
cache.init_app(app)
#celery.init_app(app)
app.app_context().push()

api.add_resource(getServices, '/getServices')
api.add_resource(getServicesAdmin, '/getServicesAdmin')
api.add_resource(getCustomers, '/getCustomers')
api.add_resource(getServicers, '/getServicers')
api.add_resource(getServicersCustomer, '/getServicersCustomer/<string:sCat_id>')
api.add_resource(getServiceRequest, '/getServiceRequest')
api.add_resource(blockCustomerAdmin, '/adminDashboard/customerBlock/<string:cust_id>')
api.add_resource(toggleServicerAdmin, '/adminDashboard/servicerToggle/<string:servicer_id>')
api.add_resource(homePageAPI, '/api/welcome')
api.add_resource(customerSignUp, '/customerSignUp')
api.add_resource(customerLogin, '/customerLogin')
api.add_resource(customerDashboard, '/customerDashboard')
api.add_resource(getCustomerDetails,'/customerDashboard/getDetails')
api.add_resource(customerServiceRequest, '/customerDashboard/serviceRequest')
api.add_resource(deleteCustomerRequest, '/customerDashboard/deleteRequest/<string:serReq_id>')
api.add_resource(updateCustomerRequest, '/customerDashboard/updateRequest')
api.add_resource(customerSearch, '/customerDashboard/search')
api.add_resource(customerSummary, '/customerDashboard/summary')
api.add_resource(adminLogin, '/adminLogin')
api.add_resource(adminDashboard, '/adminDashboard')
api.add_resource(adminNewService, '/adminDashboard/new_service')
api.add_resource(adminEditService, '/adminDashboard/new_service/<int:service_id>')
api.add_resource(adminCustomer, '/adminDashboard/customer')
api.add_resource(adminSearch, '/adminDashboard/search')
api.add_resource(adminSummary, '/adminDashboard/summary')
api.add_resource(servicerLogin, '/servicerLogin')
api.add_resource(servicerSignUp, '/servicerSignUp')
api.add_resource(getServiceRequestsServicer, '/servicerDashboard/serviceRequests')
api.add_resource(updateRequestServicer, '/servicerDashboard/updateRequestServicer')
api.add_resource(closeServiceCutomer, '/servicerDashboard/closeServiceCutomer')

@app.route("/test_cache")
@cache.cached(timeout=10)
def test_cache():
    time.sleep(10)
    return "Test works"

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