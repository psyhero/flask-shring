import datetime

from sqlalchemy import Column,Integer,String,Float,Boolean,DateTime,PickleType,Date

from .extentions import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(16),unique=True)
    password = db.Column(db.String(12))
    create_date = db.Column(db.DateTime,default=datetime.datetime.now)
    email = db.Column(db.String(25),unique=True,nullable=False)
    mobile = db.Column(db.Integer,unique=True)
    avatar = db.Column(db.String(255))

class Order(db.Model):
    __tablename__ = 'order'
    order_no = db.Column(db.String(36),primary_key=True)
    total_fee = db.Column(db.Float,default=0.01)
    subject = db.Column(db.String(55))
    uid = db.Column(db.String(36))
    url = db.Column(db.String(255))
    amount = db.Column(db.Integer)
    create_date = db.Column(db.DateTime,default=datetime.datetime.now)
    paid = db.Column(db.Boolean,default=False)
    status = db.Column(db.Boolean,default=False)
    comment = db.Column(db.String(10))

class Proxy(db.Model):
    __tablename__ = 'proxy'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    ip = db.Column(db.String(20))
    port = db.Column(db.Integer)
    protocol = db.Column(db.String(10),default='HTTP')
    last_check_time = db.Column(db.DateTime)

class UserAgent(db.Model):
    __tablename__ = 'user_agent'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_agent = Column(String(500))

class VideoPlay(db.Model):
    __tablename__ = 'video_play'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    oid = db.Column(db.String(36))
    url = db.Column(db.String(255))
    proxy = db.Column(db.String(25))
    user_agent = db.Column(db.String(500))
    create_date = db.Column(db.DateTime,default=datetime.datetime.now)
    play_time = db.Column(db.Integer)
