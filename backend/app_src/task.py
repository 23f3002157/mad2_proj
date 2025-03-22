from celery import Celery
from celery.schedules import crontab
from .worker import celery
from .models import *
from jinja2 import Template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .models import db, CustomerDetails, Service, ServiceCategory, Servicer, ServiceRequest, Feedback

def send_mail(email,email_content):
    smtp_server_host = "localhost"
    smtp_port = 1025
    sender_email = "admin@gmail.com"
    sender_password = ""

    # Set up email server
    server = smtplib.SMTP(host=smtp_server_host, port=smtp_port)
    server.login(sender_email, sender_password)
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = "Remainders - Pending Service Requests"

    # Attach the HTML content to the email
    msg.attach(MIMEText(email_content, "html"))
    server.sendmail(sender_email, email, msg.as_string())
    print("Mail Sent")


def get_html_report(data, name, filename):
    with open("app_src/"+filename+".html", "r") as file:
        jinja_template = Template(file.read())
        html_report = jinja_template.render({"user":name,"data":data})
        return html_report

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    #sender.add_periodic_task(30.0, daily_remainder.s(), name='add every 30')
    sender.add_periodic_task(
        crontab(hour=1, minute=11),
        daily_remainder.s(),
        name="Daily Remainder at 6:30 PM"
    )
    sender.add_periodic_task(
        crontab(hour=1, minute=16, day_of_month='23'),
        monthly_reminder.s(),
        name="Monthly Customer Reminder"
    )

@celery.task
def test(arg):
    print(arg)

@celery.task
def daily_remainder():
    serProf = Servicer.query.all()
    for curr in serProf:
        s1=ServiceRequest.query.filter_by(servicer_id=curr.servicer_ID).all()
        if s1:
            pendingRequests = []
            for serReq in s1:
                if serReq.status == "REQUESTED":
                    s2=Service.query.filter_by(service_ID=serReq.service_id).first()
                    print(s2.service_Description)
                    d=serReq.convert_to_json()
                    d["service_Description"] = s2.service_Description
                    pendingRequests.append(d)
            
            report = get_html_report(pendingRequests, curr.firstname+" "+curr.lastname, "report")
            send_mail(curr.email, report)


@celery.task
def monthly_reminder():
    c=CustomerDetails.query.all()
    for cust in c:
        cust_ids = cust.cust_id
        s1 = ServiceRequest.query.filter_by(cust_id=cust_ids).all()
        if s1:
            service_requests = []
            for i in s1:
                s2 = Service.query.filter_by(service_ID=i.service_id).first()
                x=s2.service_Description
                d=i.convert_to_json()
                d['service_Description'] = x
                service_requests.append(d)
            report = get_html_report(service_requests, cust.name, "cust_report")
            send_mail(cust.email, report)