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
    
class getServiceRequest(Resource):
    @jwt_required()
    def get(self):
        cust_id = get_jwt_identity()
        s=ServiceRequest.query.filter_by(cust_id=cust_id).all()
        l=[]
        for cat in s:
            s2 = Service.query.filter_by(service_ID=cat.service_id).first()
            d=cat.convert_to_json()
            d["service_Description"] = s2.service_Description   
            l.append(d)
        return l, 200
class getServices(Resource):
    def get(self):
        s=ServiceCategory.query.all()
        l=[]
        for cat in s:    
            l.append(cat.convert_to_json())
        return l, 200
    
class getServicesAdmin(Resource):
    def get(self):
        s=Service.query.all()
        l=[]
        for cat in s:
            s2=ServiceCategory.query.filter_by(sCat_id=cat.sCat_id).first()
            d=cat.convert_to_json()
            d["ser_desc"]=s2.ser_desc    
            l.append(d)
        return l, 200

class getServicersCustomer(Resource):
    def get(self, sCat_id):
        s=Servicer.query.filter_by(sCat_id=sCat_id).all()
        l=[]
        for cat in s:
            if cat.status==1:    
                l.append(cat.convert_to_json())
        return l, 200
    
class getCustomers(Resource):
    def get(self):
        s=CustomerDetails.query.all()
        l=[]
        for cat in s:    
            l.append(cat.convert_to_json())
        return l, 200

class getServicers(Resource):
    def get(self):
        s=Servicer.query.all()
        l=[]
        for cat in s:    
            l.append(cat.convert_to_json())
        return l, 200

class blockCustomerAdmin(Resource):
    @jwt_required()
    def put(self, cust_id):
        print(get_jwt_identity())
        if get_jwt_identity() != "admin@1234":
            return {"message":"Unauthorized access!"}, 401
        cust = CustomerDetails.query.get(cust_id)
        if cust:
            cust.flags=1
            db.session.commit()
            return {"message":f"Customer {cust.name} blocked successfully!"}, 200
        else:
            return {"message":"Customer not found!"}, 404
    
    @jwt_required()
    def patch(self, cust_id):
        print(get_jwt_identity())
        if get_jwt_identity() != "admin@1234":
            return {"message":"Unauthorized access!"}, 401
        cust = CustomerDetails.query.get(cust_id)
        if cust:
            cust.flags=0
            db.session.commit()
            return {"message":f"Customer {cust.name} unblocked successfully!"}, 200
        else:
            return {"message":"Customer not found!"}, 404

class toggleServicerAdmin(Resource):
    @jwt_required()
    def put(self, servicer_id):
        print(get_jwt_identity())
        if get_jwt_identity() != "admin@1234":
            return {"message":"Unauthorized access!"}, 401
        servicer = Servicer.query.get(servicer_id)
        if servicer:
            print(servicer.flag)
            if servicer.flag==1:
                servicer.flag=0
            else:    
                servicer.flag=1
            servicer.modified_date=datetime.now()
            db.session.commit()
            return {"message":f"Servicer toggled successfully!"}, 200
        else:
            return {"message":"Servicer not found!"}, 404
    @jwt_required()
    def delete(self, servicer_id):
        servicer = Servicer.query.get(servicer_id)
        if servicer:
            db.session.delete(servicer)
            db.session.commit()
            return {"message":"Servicer deleted successfully!"}, 200
        else:
            return {"message":"Servicer not found!"}, 404
        
    @jwt_required()
    def patch(self, servicer_id):
        print(get_jwt_identity())
        if get_jwt_identity() != "admin@1234":
            return {"message":"Unauthorized access!"}, 401
        servicer = Servicer.query.get(servicer_id)
        if servicer:
                servicer.status=1
                db.session.commit()
                return {"message":"Servicer Aproved successfully!"}, 200
            
class updateCustomerRequest(Resource):
    @jwt_required()
    def put(self):
        data = request.json
        cust_id = get_jwt_identity()
        s1 = data.get("serReq_id")
        s2 = ServiceRequest.query.filter_by(serReq_id=s1, cust_id=cust_id).first()
        if s2:
            x=data.get("service_date")
            s2.service_date = datetime(int(x[0:4]),int(x[5:7]),int(x[8:19]))
            db.session.commit()
            return {"message":"Service date updated successfully"}, 200
        else:
            return {"message":"Service request not found!"}, 404
class customerSearch(Resource):
    @jwt_required()
    def post(self):
        data = request.json
        print(data)
        x1=data.get("searchQuery")
        x2 = data.get("searchBy")
        if x2 == "service_description":
            s=Service.query.filter_by(service_Description=x1).all()
            l=[]
            for cat in s:    
                l.append(cat.convert_to_json())
            return {"data":l, "stat":1}, 200
        elif x2 == "price":
            s=Service.query.filter_by(price=int(x1)).all()
            l=[]
            for cat in s:    
                l.append(cat.convert_to_json())
            return {"data":l,"stat":1}, 200
        elif x2 == "category":
            s=(ServiceCategory.query.filter_by(ser_desc=x1).first())
            s1=s.sCat_id
            print(s1)
            s_main = Service.query.filter_by(sCat_id=s1).all()
            l=[]
            for cat in s_main:    
                l.append(cat.convert_to_json())
            return {"data":l, "stat":1}, 200
        else:
            return {"message":"Something went wrong", "stat":0}, 400
    
    @jwt_required()
    def put(self):
        cust_id = get_jwt_identity()
        data = request.json
        if data.get("searchBy")=="firstname":
            s=Servicer.query.filter_by(firstname=data.get("searchQuery"), status=1, flag=0).all()
            l=[]
            for cat in s:
                s2=ServiceCategory.query.filter_by(sCat_id=cat.sCat_id).first()
                d=cat.convert_to_json()
                d['ser_desc']=s2.ser_desc
                l.append(d)
            return {"data":l, "stat":1}, 200
        elif data.get("searchBy")=="city":
            s=Servicer.query.filter_by(city=data.get("searchQuery"), status=1, flag=0).all()
            l=[]
            for cat in s:
                s2=ServiceCategory.query.filter_by(sCat_id=cat.sCat_id).first()
                d=cat.convert_to_json()
                d['ser_desc']=s2.ser_desc
                l.append(d)
            return {"data":l, "stat":1}, 200
        elif data.get("searchBy")=="category":
            s2=ServiceCategory.query.filter_by(ser_desc=data.get("searchQuery")).first()
            x,y=s2.sCat_id, s2.ser_desc
            s=Servicer.query.filter_by(sCat_id=x, status=1, flag=0).all()
            l=[]
            for cat in s:
                d=cat.convert_to_json()
                d['ser_desc']=y
                l.append(d)
            return {"data":l, "stat":1}, 200
        else:
            return {"message":"Something went wrong", "stat":0}, 400

class customerSummary(Resource):
    @jwt_required()
    def get(self):
        cust_id = get_jwt_identity()
        s1=ServiceRequest.query.filter_by(cust_id=cust_id).all()
        totalRequests, totalPending, totalCompleted = 0,0,0
        d={}
        for s in s1:
            if s.status == "REQUESTED":
                totalPending+=1
            elif s.status == "COMPLETED":
                totalCompleted+=1
            
        totalRequests+=len(s1)
        return {"data_1":[totalPending, totalCompleted, totalRequests]}, 200
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
        s1=Service.query.all()
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
        return {"message":"service added successfully", "status":1}, 200

class customerServiceRequest(Resource):
    @jwt_required()
    def post(self):
        s1=ServiceRequest.query.all()
        data=request.json
        cust_id = get_jwt_identity()
        print(data, cust_id)
        sr1=data.get("service_ID")
        sr2=datetime.now()
        sr3=data.get('service_date')
        new=datetime(int(sr3[0:4]),int(sr3[5:7]),int(sr3[8:]))
        sr4=cust_id
        sr5="REQUESTED"
        sr6=data.get('servicer_ID')
        sr7 = CustomerDetails.query.filter_by(cust_id=cust_id).first().name
        sr8 = Servicer.query.filter_by(servicer_ID=sr6).first().firstname
        
        if not s1:
            sr0 = 1
        else:
            s2=s1[-1]
            s2=s2.convert_to_json()
            sr0=int(s2['serReq_id'])+1
        s=ServiceRequest(serReq_id=sr0, service_id=sr1, created_date=sr2, service_date=new, cust_id=sr4, status=sr5, servicer_id=sr6, custname=sr7, servicername=sr8, completed_date=new)
        db.session.add(s)
        db.session.commit()
        return {"message":"service request added successfully", "status":1}, 200
#         "serReq_id" VARCHAR(40) NOT NULL,
#   service_id INTEGER NOT NULL,
#   created_date DATETIME,
#   service_date DATETIME,
#   completed_date DATETIME,
#   cust_id VARCHAR(40) NOT NULL,
#   status VARCHAR(10),
#   servicer_id VARCHAR(40) NOT NULL,
#   custname VARCHAR(40),
#   servicername VARCHAR(40),
#   PRIMARY KEY ("serReq_id"),

class deleteCustomerRequest(Resource):
    @jwt_required()
    def put(self, serReq_id):
        s=ServiceRequest.query.filter_by(serReq_id=serReq_id).first()
        if s:
            db.session.delete(s)
            db.session.commit()
            return {"message":"service request deleted successfully", "status":1}, 200
        else:
            return {"message":"service request not found", "status":0}, 404


class adminEditService(Resource):
    @jwt_required()
    def put(self, service_id):
        s=Service.query.filter_by(service_ID=service_id).first()
        if s:
            db.session.delete(s)
            db.session.commit()
            return {"message":"service deleted successfully", "status":1}, 200
        else:
            return {"message":"service not found", "status":0}, 404
    
    @jwt_required()
    def patch(self, service_id):
        data = request.json
        s=Service.query.filter_by(service_ID=data.get("service_ID")).first()
        if s:
            s.service_Description=data.get("service_description")
            s.price=data.get("price")
            s.sCat_id=data.get("sCat_id")
            s.modified_date=datetime.now()
            db.session.commit()
            return {"message":"service updated successfully", "status":1}, 200
        else:
            return {"message":"service not found", "status":0}, 404
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

class adminSearch(Resource):
    @jwt_required()
    def post(self):
        data = request.json
        print(data)
        if data.get("searchBy")=="firstname":
            s=Servicer.query.filter_by(firstname=data.get("searchQuery")).all()
            l=[]
            for cat in s:
                s2=ServiceCategory.query.filter_by(sCat_id=cat.sCat_id).first()
                d=cat.convert_to_json()
                d['ser_desc']=s2.ser_desc
                l.append(d)
            return {"data":l, "stat":1}, 200
        elif data.get("searchBy")=="city":
            s=Servicer.query.filter_by(city=data.get("searchQuery")).all()
            l=[]
            for cat in s:
                s2=ServiceCategory.query.filter_by(sCat_id=cat.sCat_id).first()
                d=cat.convert_to_json()
                d['ser_desc']=s2.ser_desc
                l.append(d)
            return {"data":l, "stat":1}, 200
        elif data.get("searchBy")=="category":
            s2=ServiceCategory.query.filter_by(ser_desc=data.get("searchQuery")).first()
            x,y=s2.sCat_id, s2.ser_desc
            s=Servicer.query.filter_by(sCat_id=x).all()
            l=[]
            for cat in s:
                d=cat.convert_to_json()
                d['ser_desc']=y
                l.append(d)
            return {"data":l, "stat":1}, 200
        else:
            return {"message":"Something went wrong", "stat":0}, 400

class adminSummary(Resource):
    @jwt_required()
    def get(self):
        c=CustomerDetails.query.all()
        s1=ServiceRequest.query.all()
        totalCustomers=len(c)
        requested, rejected, accepted, completed = 0,0,0,0
        s1=ServiceRequest.query.all()
        for i in s1:
            if i.status=="REQUESTED":
                requested+=1
            elif i.status=="REJECTED":
                rejected+=1
            elif i.status=="ACCEPTED":
                accepted+=1
            elif i.status=="COMPLETED":
                completed+=1
        c_1=CustomerDetails.query.filter_by(flags=1).all()
        blockedCust, activeCust = len(c_1), totalCustomers-len(c_1)
        return {"data_1":[requested, rejected, accepted, completed], "data_2":[blockedCust, activeCust]}, 200


class getCustomerDetails(Resource):
    @jwt_required()
    def get(self):
        cust_id = get_jwt_identity()
        print(cust_id)
        s=CustomerDetails.query.filter_by(cust_id=cust_id).first()
        l=s.convert_to_json()
        print([l])
        return {"message":"Customer details", "data":[l]}, 200

class customerLogin(Resource):
    def post(self):
        data = request.get_json()
        if not(data.get('email') and data.get('cust_password')):
            return {"message":"Missing fields, try again!"}, 400
        c = CustomerDetails.query.filter_by(email=data.get("email")).first()
        if c:
            if c.flags==1:
                return {"message":"Customer blocked, contact administrator"}, 400
            else:
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
                    if ser.flag==1:
                        return {"message":"Servicer blocked, contact administrator"}, 400
                    else:
                        token = create_access_token(ser.servicer_ID)
                        return {"message":"Servicer login successful!","token":token,"username":ser.firstname+" "+ser.lastname,"email":ser.email, "login": 1}, 200
                else:
                    return {"message":"Inccorect password"},400
                
class getServiceRequestsServicer(Resource):
    @jwt_required()
    def get(self):
        servicer_id=get_jwt_identity()
        print(servicer_id)
        s1=ServiceRequest.query.filter_by(servicer_id=servicer_id).all()
        l=[]
        for s in s1:
            l.append(s.convert_to_json())
        return {"data":l, "stat":1}, 200

class updateRequestServicer(Resource):
    @jwt_required()
    def put(self):
        data = request.get_json()
        if data.get("status")=="ACCEPT":
            s=ServiceRequest.query.filter_by(servicer_id=get_jwt_identity(), serReq_id=data.get("serReq_id")).first()
            s.status="ACCEPTED"
            db.session.commit()
            return {"message":"Service request accepted successfully", "status":1}, 200
        elif data.get("status")=="REJECT":
            s=ServiceRequest.query.filter_by(servicer_id=get_jwt_identity(), serReq_id=data.get("serReq_id")).first()
            s.status="REJECTED"
            db.session.commit()
            return {"message":"Service request rejected successfully", "status":1}, 200
        
class closeServiceCutomer(Resource):
    @jwt_required()
    def post(self):
        data=request.json
        x=data.get("serReq_id")
        s=ServiceRequest.query.filter_by(serReq_id=x).first()
        s.status="COMPLETED"
        db.session.commit()
#         fid VARCHAR(40) NOT NULL,
#   "serReq_id" VARCHAR(40) NOT NULL,
#   ratings INTEGER,
#   comments VARCHAR(100),
        f=Feedback(fid=random.randint(10000,99999),serReq_id=x,ratings=int(data.get("rating")), comments=data.get("comment"))
        s1=Servicer.query.filter_by(servicer_ID=data.get("servicer_id")).first()
        if s1.rating==0:
            s1.rating=int(data.get("rating"))
        else:
            x=(s1.rating+int(data.get("rating")))/2
            s1.rating=x
        db.session.add(f)
        db.session.commit()
        return {"message":"Service request completed successfully", "status":1}, 200
    
