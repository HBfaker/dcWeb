#!/usr/bin/env python  
# -*- coding:utf-8 -*- 

""" 
@version: v1.0 
@author: Harp
@contact: liutao25@baidu.com 
@software: PyCharm 
@file: manage.py 
@time: 2018/1/14 0014 13:00 
"""

from app import app
from app import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


