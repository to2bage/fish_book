from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user

from . import web
from app.forms.auth import RegisgerForm, LoginForm
from app.models.user import User
from app.models.base import db


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisgerForm(request.form)
    if request.method == "POST" and form.validate():
        with db.auto_commit():
            user = User()
            user.set_attr(form.data)
            db.session.add(user)
        return redirect(url_for("web.login"))
        pass
    return render_template("auth/register.html", form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_pwd(form.password.data):
            login_user(user)
            pass
        else:
            flash("登录的电子邮件不存在或者密码错误,请重新登录")
        pass
    return render_template("auth/login.html", form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass

@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass


@web.route('/register/confirm/<token>')
def confirm(token):
    pass
    # if current_user.confirmed:
    #     return redirect(url_for('main.index'))
    # if current_user.confirm(token):
    #     db.session.commit()
    #     flash('You have confirmed your account. Thanks!')
    # else:
    #     flash('The confirmation link is invalid or has expired.')
    # return redirect(url_for('main.index'))


@web.route('/register/ajax', methods=['GET', 'POST'])
def register_ajax():
    pass


