from flask_mail import Message
from flask import render_template
from . import mail


def mail_message(subject,template,to,**kwargs):  #taking four parameters
    sender_email = "ryanmiano68@gmail.com"

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.txt = render_template(template + ".txt",**kwargs)
    mail.send(email)
