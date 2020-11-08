from libs.orm import db

class User(db.Model):
	__tablename__ = 'user'

	id = db.Column(db.Integer,primary_key=True)
	nickname = db.Column(db.String(20),unique=True)
	password = db.Column(db.String(128),nullable=False)
	gender = db.Column(db.Enum('male', 'female', 'unknow'),default='unknow')
	birthday = db.Column(db.Date,default='2020-01-01')
	city = db.Column(db.String(10),default='中国')
	avatar = db.Column(db.String(256),default='/static/img/default.png')
	bio = db.Column(db.Text,default='好懒，什么也没有留下')
	created = db.Column(db.DateTime,nullable=False)







