
from flask import Blueprint,request

from ..models import Order
# from ..extentions import alipay

bpay = Blueprint('pay',__name__)

@bpay.route('/alipay',methods=['GET','POST'])
def alipay():
    oid = request.args.get('oid')
    order = Order.query.filter(Order.order_no == oid).first()
    response = alipay.pay_order(order)
    return response

    
@bpay.route('/ali_notify', methods=['POST'])
def notify():

    return 'failure'
