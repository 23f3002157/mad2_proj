from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Integer, String, Boolean, Float
db = SQLAlchemy()

class ServiceCategory(db.Model):
    __tablename__ = 'service_categories'
    sCat_id = db.Column(db.String(40), primary_key=True)
    ser_desc = db.Column(db.String(140), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    services = db.relationship('Service', back_populates='category')

    def convert_to_json(self):
        return {
            "sCat_id":self.sCat_id, "ser_desc":self.ser_desc, "created_date":str(self.created_date)[:-6]
        }

class Service(db.Model):
    __tablename__ = 'Service'
    service_ID = db.Column(Integer, primary_key=True)
    service_Description = db.Column(String(40), nullable=False)
    price = db.Column(db.Float, nullable=False)
    sCat_id = db.Column(db.String(40), db.ForeignKey('service_categories.sCat_id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    modified_date = db.Column(db.DateTime)
    category = db.relationship('ServiceCategory', back_populates='services')
    service_requests = db.relationship('ServiceRequest', back_populates='service')

    def convert_to_json(self):
        return {
            "service_ID":self.service_ID, "service_description":self.service_Description,
            "price":self.price, "sCat_id":self.sCat_id, "created_date":str(self.created_date), "modified_date":str(self.modified_date)
        }
class Servicer(db.Model):
    __tablename__ = 'Servicer'
    servicer_ID = db.Column(db.String(40), primary_key=True)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    pass_ = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    state = db.Column(db.String(40), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    modified_date = db.Column(db.DateTime, nullable=False)
    sCat_id = db.Column(db.String(40), db.ForeignKey('service_categories.sCat_id'), nullable=False)
    flag = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)
    document_verify = db.Column(db.LargeBinary)
    servicer_photo = db.Column(db.LargeBinary)
    experience = db.Column(db.Integer)
    rating = db.Column(Float, default=0)
    category = db.relationship('ServiceCategory', backref='servicers')
    service_requests = db.relationship('ServiceRequest', back_populates='servicer')

    def convert_to_json(self):
        return {
            "servicer_ID":self.servicer_ID, "firstname":self.firstname,"lastname":self.lastname,"email":self.email,
            "pass_":self.pass_,"address":self.address, "city":self.city, "state":self.state, "created_date":str(self.created_date),
            "modified_date":str(self.modified_date),"sCat_id":self.sCat_id, "flag":self.flag, "status":self.status, "experience":self.experience,
            "rating":self.rating
        }
class CustomerDetails(db.Model):
    __tablename__ = 'customerDetails'
    cust_id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    cust_password = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    modified_date = db.Column(db.DateTime, nullable=False)
    flags = db.Column(db.Integer, default=0)
    city = db.Column(db.String(40), nullable=False)
    rating = db.Column(Float, default=0)
    service_requests = db.relationship('ServiceRequest', back_populates='customer')

    def convert_to_json(self):
        return {"cust_id":self.cust_id, "name":self.name, "email":self.email, "cust_password":self.cust_password, "address":self.address,
                "postcode":self.postcode,"create_date":str(self.create_date), "modified_date":str(self.modified_date), "flag":self.flags,"city":self.city,
                "rating":self.rating}
class Feedback(db.Model):
    __tablename__ = 'feedback'
    fid = db.Column(db.String(40), primary_key=True)
    serReq_id = db.Column(db.String(40), db.ForeignKey('service_request.serReq_id'), nullable=False)
    ratings = db.Column(db.Integer)
    comments = db.Column(db.String(100))
    service_request = db.relationship('ServiceRequest', back_populates='feedback')

class ServiceRequest(db.Model):
    __tablename__ = 'service_request'
    serReq_id = db.Column(db.String(40), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('Service.service_ID'), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now())
    service_date = db.Column(db.DateTime)
    completed_date = db.Column(db.DateTime)
    cust_id = db.Column(db.String(40), db.ForeignKey('customerDetails.cust_id'), nullable=False)
    status = db.Column(db.String(10))
    servicer_id = db.Column(db.String(40), db.ForeignKey('Servicer.servicer_ID'), nullable=False)
    custname = db.Column(db.String(40))
    servicername = db.Column(db.String(40))
    service = db.relationship('Service', back_populates='service_requests')
    customer = db.relationship('CustomerDetails', back_populates='service_requests')
    servicer = db.relationship('Servicer', back_populates='service_requests')
    feedback = db.relationship('Feedback', back_populates='service_request', uselist=False)

    def convert_to_json(self):
        return {
            "serReq_id":self.serReq_id, "service_id":self.service_id, "created_date":str(self.created_date),
            "service_date":str(self.service_date), "completed_date":str(self.completed_date), "cust_id": self.cust_id,
            "status":self.status, "servicer_id":self.servicer_id, "custname":self.custname, "servicername": self.servicername
        }