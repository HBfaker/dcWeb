# -*- coding: UTF-8 -*-

from app import app
from ..models import db,Admin

@app.route('/')
def home():
    admin = Admin(username='老哥',password='dada')
    db.session.add(admin)
    db.session.commit()
    return "hello,world!"
