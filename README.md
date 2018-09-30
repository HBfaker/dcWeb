该版本在dcWeb_1_0的基础上，将项目目录更改为flask标准目录。

dcWeb_2_0:
app —— flask程序保存在此文件夹下
     --static —— 存放公共css\js\images等静态文件
     --templates ——存放html\Jinja2模板
     --__init__.py
     --models.py —— 数据库代码
     --views.py —— 视图文件，路由
migrations —— 包含数据库迁移脚本（安装flask-migrate后自动生成）
tests —— 单元测试存放在此文件夹下
venv —— python虚拟环境
config.py —— 存储配置变量
requirements.txt —— 列出了所有的依赖包，以便于在其他电脑中重新生成相同的环境
manage.py —— 启动程序或者其他任务
run.py —— 程序入口

运行：
安装所有的依赖包；
建立一个mysql数据库，修改config.py中的相关参数；
运行run.py

测试一下能不能提交！！！hello,world