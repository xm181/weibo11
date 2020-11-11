# 写注释啊，别打错别字啊
from libs.orm import db


class Weibo(db.Model):
	__tablename__ = 'weibo'

	id = db.Column(db.Integer, primary_key=True)
	uid = db.Column(db.Integer,nullable=False,index=True)
	content = db.Column(db.Text,nullable=False)
	created = db.Column(db.DateTime,nullable=False)
	updated = db.Column(db.DateTime,nullable=False)