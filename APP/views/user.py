import random

from flask import Blueprint,render_template,redirect,request,session,jsonify
from sqlalchemy import or_

from ..extentions import db,pool
from ..models import User
from ..worker import vertify_mail

buser = Blueprint('user',__name__)

@buser.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('user/register.html')
    
    email = request.form.get('email')
    vertify = request.form.get('vertify')
    username = request.form.get('username')
    password = request.form.get('password')
    vtf_email = session.get('vtf_email')
    vtf_code = session.get('vtf_code')
    if vertify != str(vtf_code) or vtf_email != email:
        return render_template('user/register.html',email=email,username=username,password=password,error='验证失败，请重试')
    
    user = User(
        email = email,
        username = username,
        password = password
    )
    try:
        db.session.add(user)
        db.session.commit()
        session.pop('vtf_email')
        session.pop('vtf_code')
        return redirect(f'/login?email={email}')
    except:
        db.session.rollback()
        db.session.flush()
        return render_template('user/register.html',error='注册失败，请重试')

@buser.route('/register/mail-vertify')
def vertical():
    email = request.args.get('email')
    user = User.query.filter(User.email == email).first()
    if user:
        return jsonify({'status':100,'message':'该邮箱已注册'})
    vtf_code = random.randint(1000,9999)
    res = {}
    try:
        pool.submit(vertify_mail,email,vtf_code)
        session['vtf_code'] = vtf_code
        session['vtf_email'] = email
        res['status'] =200
        res['message'] = '邮件已发送'
    except:
        res['status'] =300
        res['message'] = '邮件发送失败,请重试'
    return jsonify(res)

@buser.route('/register/username-vertify')
def username_vertify():
    username = request.args.get('username')
    user = User.query.filter(User.username == username).first()
    if user:
        return jsonify({'status':100,'message':'该昵称已存在'})
    else:
        return jsonify({'status':200,'message':''})

@buser.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        email = request.args.get('email')
        return render_template('user/login.html',email=email)
    elif request.method == 'POST':
        account = request.form.get('account')
        pwd = request.form.get('password')
        user = User.query.filter(or_(User.email == account,User.username == account),User.password == pwd).first()
        if user :
            info = user.username
            response = redirect('/')
            response.set_cookie('user',info,max_age=3600*24*7)
            return response
        else:
            error = '账号信息错误，请重新输入'
            return render_template('user/login.html',account=account,error=error)

@buser.route('/logout')
def logout():
    response = redirect('/')
    response.delete_cookie('user')
    return response