import time
import uuid

from flask import Blueprint,render_template,request,redirect

from ..extentions import db,pool
from ..models import User,Order
from ..worker import order_status_check,play_video

border = Blueprint('order',__name__)

@border.route('/order',methods=['GET','POST'])
def order():
    if request.method == 'GET':
        account = request.cookies.get('user')
        return render_template('order.html',account=account)
    
    username = request.cookies.get('user')
    user = User.query.filter(User.username == username).first()
    if user:
        timestamp = time.time()
        amount = request.form.get('amount'),
        new_order = Order(
            order_no = str(int(timestamp))+str(uuid.uuid4())[-6:],
            total_fee = float(amount[0]) * 0.01,
            subject = f'{user.username}的订单',
            uid = user.id,
            url = request.form.get('url'),
            amount = amount[0]
        )
        try:
            db.session.add(new_order)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
        pool.submit(play_video,new_order.order_no,new_order.url,new_order.amount)
        response = redirect('/myorder')
        return response

@border.route('/myorder')
def myorder():
    account = request.cookies.get('user')
    user = User.query.filter(User.username == account).first()
    order_status_check(user)
    page = int(request.args.get('page',1))
    paginate = Order.query.filter(Order.uid == user.id).order_by(-Order.create_date).paginate(page=page,per_page=5,error_out=False)
    return render_template(
        'user/myorder.html',
        account=account,
        orders=paginate
    )
