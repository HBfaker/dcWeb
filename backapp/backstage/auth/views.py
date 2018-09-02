import sys

from flask import render_template, redirect, request, url_for, flash, session

# from dcWeb_2_0 import app
# from dcWeb_2_0.app.newmodels import Admin, SuperAdmin, db
from app.models import SuperAdmin, db

from . import auth
from .forms import LoginForm

#
# sys.path.append(r"D:\lucy\研一下\大创xinyu\dachuangwebsite\dcWeb_2_0")
# from  app.newmodels import  Admin





from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.rememberme.data)
    if form.validate_on_submit():
            user= db.session.query(SuperAdmin).filter_by(username=form.username.data).first()
            # user = SuperAdmin.query.filter_by(username=form.username.data).first()
            print(user)

            # return redirect(url_for('main.index'))
            if user is not None and user.password == form.password.data:
                # session['username'] = user.username
                # session.permanent = True
                login_user(user, form.rememberme.data)
                print("11111")
                flash("登录成功")
                return redirect(request.args.get('next') or url_for('main.index'))
            else:
                print("2222")
                flash('用户名或密码错误')


    return  render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    # session.clear()
    flash('您已退出登录')
    return redirect(url_for('auth.login'))
