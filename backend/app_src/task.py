from celery import Celery
from celery.schedules import crontab
from .worker import celery
from .models import *
from jinja2 import Template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(email,email_content):
    smtp_server_host = "localhost"
    smtp_port = 1025
    sender_email = "admin@email.com"
    sender_password = ""

    # Set up email server
    server = smtplib.SMTP(host=smtp_server_host, port=smtp_port)
    server.login(sender_email, sender_password)
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = "Remainders"

    # Attach the HTML content to the email
    msg.attach(MIMEText(email_content, "html"))
    server.sendmail(sender_email, email, msg.as_string())
    print("Mail Sent")


def get_html_report(user, data):
    with open("app_src/report.html", "r") as file:
        jinja_template = Template(file.read())
        html_report = jinja_template.render({"user":"helo","data":"data"})
        return html_report

@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')
    sender.add_periodic_task(30.0, daily_remainder.s(), name='add every 30')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=18, minute=30),
        daily_remainder.s(),
        name="Daily Remainder at 6:30 PM"
    )

@celery.task
def test(arg):
    print(arg)

@celery.task
def daily_remainder():
    customer = CustomerDetails.query.all()
    for cust in customer:
        print(cust.convert_to_json())
    x=cust
    html_report = get_html_report("hello", "there")
    send_mail("risshabsrinivas@gmail.com",html_report)
    print(x.name)

