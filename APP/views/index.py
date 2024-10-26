
from flask import Blueprint,render_template,request

blue = Blueprint('home',__name__)

@blue.route('/',methods=['GET','POST'])
def index():
    account = request.cookies.get('user')
    return render_template('index.html',account=account)
