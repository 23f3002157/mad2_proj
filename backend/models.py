from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ServiceCategory(db.Model):
    __tablename__ = 'service_categories'
    sCat_id = db.Column(db.String(40), primary_key=True)
    ser_desc = db.Column(db.String(140), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    services = db.relationship('Service', back_populates='category')

class Service(db.Model):
    __tablename__ = 'Service'
    service_ID = db.Column(db.Integer, primary_key=True)
    service_Description = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Float, nullable=False)
    sCat_id = db.Column(db.String(40), db.ForeignKey('service_categories.sCat_id'), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_date = db.Column(db.DateTime)
    category = db.relationship('ServiceCategory', back_populates='services')
    service_requests = db.relationship('ServiceRequest', back_populates='service')

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
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_date = db.Column(db.DateTime, nullable=False)
    sCat_id = db.Column(db.String(40), db.ForeignKey('service_categories.sCat_id'), nullable=False)
    flag = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)
    document_verify = db.Column(db.LargeBinary)
    servicer_photo = db.Column(db.LargeBinary)
    experience = db.Column(db.Integer)
    category = db.relationship('ServiceCategory', backref='servicers')
    service_requests = db.relationship('ServiceRequest', back_populates='servicer')

class CustomerDetails(db.Model):
    __tablename__ = 'customerDetails'
    cust_id = db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    cust_password = db.Column(db.String(40), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modified_date = db.Column(db.DateTime, nullable=False)
    flags = db.Column(db.Integer, default=0)
    city = db.Column(db.String(40), nullable=False)
    service_requests = db.relationship('ServiceRequest', back_populates='customer')

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
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
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
