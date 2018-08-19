from flask import Flask
from .models import db  # 数据库
app = Flask(__name__)   # 新建一个flask应用
app.config.from_object('config')  # 将配置文件导入应用中
db.init_app(app)

#from . import view  # 导入视图
from .view import views