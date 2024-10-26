import random
import time

from flask_mail import Message
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .config import MAIL_USERNAME
from .decorator import save_to_videoplay
from .extentions import mail,db,pool
from .models import Order,Proxy,UserAgent,VideoPlay

def vertify_mail(email,vtf_code):
    from APP import create_app
    with create_app().app_context():
        msg = Message('Flask 邮箱验证码',sender=MAIL_USERNAME,recipients=[email])
        msg.body = f'Welcome to join Flask.\nHere is your vertications: \n\n{vtf_code}'
        mail.send(msg)

def order_status_check(user):
    orders = Order.query.filter(Order.uid == user.id).all()
    for it in orders:
        plays = VideoPlay.query.filter(VideoPlay.oid == it.order_no).all()
        if it.amount == len(plays):
            it.paid =1
            it.status =1
        ts = time.time()
        timestamp = (it.create_date).timestamp()
        if it.paid == 0 and it.status == 0 and (ts - timestamp) > 600:
            it.comment = '已超时'
        elif it.paid == 1 and it.status == 0:
            it.comment = '进行中'
            db.session.commit()
        elif it.status == 1:
            it.comment = '已完成'
            db.session.commit()

@save_to_videoplay
def play_video(oid,url,amount):
    pid = Proxy.query.first().id
    data = []
    while amount:
        index = random.randint(21,40)
        user_agent = UserAgent.query.filter(UserAgent.id == index).first()
        try:
            proxy = get_proxy(pid)
            result = pool.submit(video_driver,oid,url,user_agent.user_agent,proxy).result()
            data.append(result)
            pid += 1
            amount -= 1
        except:
            pid += 1
            continue
    return data

def get_proxy(pid):
    proxy= Proxy.query.filter(Proxy.id == {pid}).first()
    return f'{proxy.ip}:{proxy.port}'

def video_driver(oid,url,user_agent,proxy):
    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(options=opts)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": user_agent})
    # driver.get(url)
    seconds = random.randint(10,30)
    # time.sleep(seconds)

    return {
        'oid' : oid,
        'url' : url,
        'proxy' : proxy,
        'user_agent' : user_agent,
        'play_time' : seconds
    }
