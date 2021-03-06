from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#超级管理员
class SuperAdmin(db.Model):
    __tablename__ = 'super_admin'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(32),index=True,unique=True,nullable=False)
    password = db.Column(db.String(128), nullable=False)
    register_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

#管理员
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    username = db.Column(db.String(32),index=True,unique=True,nullable=False)
    password = db.Column(db.String(128), nullable=False)
    register_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
#用户表对应的用户实体类
class Users(db.Model):
    __tablename__ = 'users_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32),index=True,unique=True,nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128),nullable=True)
    register_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

#发布信息

class Information(db.Model):
    __tablename__ = 'site_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256),nullable=False)
    content = db.Column(db.String(256),nullable=False)
    attachment = db.Column(db.String(256), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

#政策文件
class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256), nullable=False)
    link = db.Column(db.String(256), index=True,unique=True,nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

#项目
class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pname = db.Column(db.String(256), nullable=False)
    team_info = db.Column(db.String(1024), nullable=True)
    introduction = db.Column(db.String(8*1024), nullable=False)
    picture = db.Column(db.String(1024), nullable=True)
    vedio = db.Column(db.String(1024), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now)