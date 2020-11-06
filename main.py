from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from libs.orm import db

#初始化app
app = Flask(__name__)

#设置一个secret_key,用来加密
app.secret_key = r'dsfhsj23oo8r0wefoiln/kj23490uhsdlf'
#连接数据库的内容
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://guo:123456@192.144.186.212:3306/weibo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # 每次请求结束后都会自动提交数据库中的变动

#初始化manager，使用manager对app进行管理调试
manager = Manager(app)

#初始化db和migrate
db.init_app(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@app.route('/')
def home():
	return 'hello world'

if __name__ == '__main__':
	manager.run()