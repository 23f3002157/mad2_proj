from flask import request, current_app as app
from flask_restful import Resource, Api
from .models import *
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from .models import db, CustomerDetails, Service, ServiceCategory, Servicer, ServiceRequest, Feedback
import random


class homePageAPI(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        msg = f"Hello from homePageAPI: {data.get('name')}"
        return {"message": msg}, 200
    def get(self):
        s=ServiceCategory.query.all()
        l=[]
        for cat in s:
            l.append(cat.convert_to_json())
        print(l)
        msg = f"Hello from homePageAPI get method household service:"
        return {"message": msg, "data":l}, 200
    

class adminLogin(Resource):
    def get(self):
        return {"message":"Welcome, admin!"},200
    def post(self):
        data = request.get_json()
        if data.get('email')=='admin@gmail.com' and data.get('password') == '1234':
            token = create_access_token("admin@1234")
            return {"message":"Admin Login Successful","token":token,"key":"admin@1234"}, 200
        else:
            return {"message":"Incorrect email id/password, try again!"}, 400
        
class adminDashboard(Resource):
    @jwt_required()
    def get(self):
        print(get_jwt_identity())
        return {"message":"welcome, admin"}, 200


class customerLogin(Resource):
    def post(self):
        data = request.get_json()
        if not(data.get('email') and data.get('cust_password')):
            return {"message":"Missing fields, try again!"}, 400
        c = CustomerDetails.query.filter_by(email=data.get("email")).first()
        if c:
            if c.cust_password == data.get("cust_password"):
                token = create_access_token({"cust_id":c.cust_id})
                return {"message":"Customer login successful!","token":token,"username":c.name,"email":c.email}, 200
            else:
                return {"message":"Incorrect Password!"}, 400
        else:
            return {"message":"User does not exist, please register"}, 404

class customerSignUp(Resource):
    def post(self):
        data = request.get_json()
        if data.get('name') and data.get('email') and data.get('cust_password') and data.get('address') and data.get("postcode") and data.get("city"):
            c = CustomerDetails.query.filter_by(email=data.get("email")).first()
            if c:
                return {"message":"Customer exists, try again!"}, 400
            else:
                if len(data.get('cust_password'))>20:
                    return {"message":"Password too long, try again"}, 400
                elif len(data.get('cust_password'))<8:
                    return {"message":"Password must be greater than 8 characters"}, 400
                else:
                    x = random.randint(10000,99999)
                    new_Customer=CustomerDetails(cust_id=str(x)+data.get('name'), name=data.get("name"), email = data.get("email"), cust_password=data.get("cust_password"),
                                                address=data.get("address"),postcode=data.get("postcode"), create_date=datetime.now(), modified_date=datetime.now(),
                                                flags=0,city=data.get("city"), rating=0)
                    db.session.add(new_Customer)
                    db.session.commit()
                    return {"message":"Customer sign up successful"}, 200
        else:
            return {"message":"Missing fields"}, 400


            