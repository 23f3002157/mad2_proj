from flask import request, current_app as app
from flask_restful import Resource, Api
from .models import *
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from .models import db, CustomerDetails, Service, ServiceCategory, Servicer, ServiceRequest, Feedback
import random, time
from flask_caching import Cache


cache = Cache()



class homePageAPI(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        msg = f"Hello from homePageAPI: {data.get('name')}"
        return {"message": msg}, 200
    
    @cache.cached(timeout=10)
    def get(self):
        s=CustomerDetails.query.all()
        l=[]
        for cat in s:
            l.append(cat.convert_to_json())
        print(l)
        msg = f"Hello from homePageAPI get method household service:"
        return {"message": msg, "data":l}, 200
    
class getServices(Resource):
    def get(self):
        s=ServiceCategory.query.all()
        l=[]
        for cat in s:    
            l.append(cat.convert_to_json())
        return l, 200
    
class adminLogin(Resource):
    def get(self):
        return {"message":"Welcome, admin!"},200
    def post(self):
        data = request.get_json()
        if data.get('email')=='admin@gmail.com' and data.get('password') == '1234':
            token = create_access_token("admin@1234")
            return {"message":"Admin Login Successful","token":token,"key":"admin@1234", "login":1}, 200
        else:
            return {"message":"Incorrect email id/password, try again!"}, 400
        
class adminDashboard(Resource):
    @jwt_required()
    def get(self):
        print(get_jwt_identity())
        return {"message":"welcome, admin"}, 200
    
class adminNewService(Resource):
    @jwt_required()
    def get(self):
        return {"message":"Form which displays various fields to create services, admin can create services"}
    
    @jwt_required()
    def post(self):
        data=request.json
        print(data)
        s1=Service.query.all()
        print(s1)
        if not s1:
            sid=1
        else:
            s2=s1[-1]
            s2=s2.convert_to_json()
            sid=s2['service_ID']+1
        s=Service(service_ID=sid, service_Description=data.get('service_Description'),price=data.get('price'), sCat_id=data.get("sCat_id"),
                  created_date=datetime.now(), modified_date=datetime.now())
        db.session.add(s)
        db.session.commit()
        return {"message":"service added successfully"}, 200
    
class adminCustomer(Resource):
    @jwt_required()
    def get(self):
        s=CustomerDetails.query.all()
        l=[]
        for cat in s:
            l.append(cat.convert_to_json())
        print(l)
        msg = f"Hello from homePageAPI get method household service:"
        return {"message": msg, "data":l}, 200

class customerLogin(Resource):
    def post(self):
        data = request.get_json()
        if not(data.get('email') and data.get('cust_password')):
            return {"message":"Missing fields, try again!"}, 400
        c = CustomerDetails.query.filter_by(email=data.get("email")).first()
        if c:
            if c.cust_password == data.get("cust_password"):
                token = create_access_token(c.cust_id)
                return {"message":"Customer login successful!","token":token,"username":c.name,"email":c.email, "login": 1}, 200
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
                    return {"message":"Customer sign up successful", "status":1}, 200
        else:
            return {"message":"Missing fields"}, 400
        
class customerDashboard(Resource):
    @jwt_required()
    def get(self):
        print(get_jwt_identity())
        return {"message":"Logged in","token":get_jwt_identity()}

class servicerSignUp(Resource):
    def post(self):
        data = request.get_json()
        if data.get('firstname') and data.get('lastname') and data.get('email') and data.get('pass_') and data.get('address') and data.get("city") and data.get("state") and data.get("experience") and data.get("document_verify") and data.get("servicer_photo") and data.get("sCat_id"):
            s = Servicer.query.filter_by(email=data.get("email")).first()
            if(s):
                return {"message":"Service provider exists, try another email","status":0}, 400
            else:
                if(len(data.get('pass_'))<8):
                    return {"message":"Password must be greater than 8 characters","status":0}, 400
                else:
                    x = random.randint(10000,99999)
                    new_servicer = Servicer(servicer_ID=str(x)+data.get('firstname'), firstname=data.get("firstname"), lastname=data.get("lastname"), email=data.get("email"), pass_=data.get("pass_"),
                                            address=data.get("address"), city=data.get("city"), state=data.get("state"), created_date=datetime.now(), modified_date=datetime.now(),
                                            sCat_id=data.get("sCat_id"), flag=0, status=0, experience=data.get("experience"), rating=0, document_verify=data.get("document_verify"), servicer_photo=data.get("servicer_photo"))
                    db.session.add(new_servicer)
                    db.session.commit()
                    return {"message":"Service provider sign up successful", "status":1}, 200
        else:
            return {"message":"Fill in all fields","status":0}, 400
        # "servicer_ID":self.servicer_ID, "firstname":self.firstname,"lastname":self.lastname,"email":self.email,
        #     "pass_":self.pass_,"address":self.address, "city":self.city, "state":self.state, "created_date":str(self.created_date),
        #     "modified_date":str(self.modified_date),"sCat_id":self.sCat_id, "flag":self.flag, "status":self.status, "experience":self.experience,
        #     "rating":self.rating, "document_verify":self.document_verify, "servicer_photo":self.servicer_photo
class servicerLogin(Resource):
    def get(self):
        return {"message":"Service Professional Login"}, 200
    def post(self):
        data = request.json
        if not(data.get('email') and data.get('pass_')):
            return {"message":"Missing fields, try again!"}, 400
        else:
            ser = Servicer.query.filter_by(email=data.get('email')).first()
            if not ser:
                return {"message":"Servicer not registered, try again later"}, 400
            elif ser.status==0:
                return {"message":"Servicer approval pending, contact administrator"}, 400
            else:
                if data.get('pass_') == ser.pass_:
                    token = create_access_token(ser.servicer_ID)
                    return {"message":"Servicer login successful!","token":token,"username":ser.firstname+" "+ser.lastname,"email":ser.email, "login": 1}, 200
                else:
                    return {"message":"Inccorect password"},400