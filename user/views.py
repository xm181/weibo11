import datetime
from sqlite3 import IntegrityError

from flask import Blueprint
from flask import redirect
from flask import request
from flask import render_template

from libs.orm import db
from user.models import User
from libs.utils import make_password
from libs.utils import save_avatar

user_bp = Blueprint(
	'user',
	__name__,
	url_prefix='/user',
	template_folder='./templates'
)


@user_bp.route('/register')
def register():
	if request.method == 'POST':
		nickname = request.form.get('nickname', '').strip()
		password1 = request.form.get('password1', '').strip()
		password2 = request.form.get('password2', '').strip()
		gender = request.form.get('gender', '').strip()
		birthday = request.form.get('birthday', '').strip()
		city = request.form.get('city', '').strip()
		bio = request.form.get('bio', '').strip()
		now = datetime.datetime.now()  # 注册时间

		if not password1 or password1 != password2:
			return render_template('register.html', err='密码不符合要求')

		user = User(nickname=nickname, password=make_password(password1),
		            gender=gender, birthday=birthday, city=city, bio=bio, created=now)

		# 保存头像
		avatar_file = request.files.get('avatar')
		if avatar_file:
			user.avatar = save_avatar(avatar_file)

		try:
			# 保存到数据库
			db.session.add(user)
			db.session.commit()
			return redirect('/user/login')
		except IntegrityError:
			db.session.rollback()
			return render_template('register.html', err='您的昵称已被占用')
	else:
		return render_template('register.html')

@user_bp.route('/login')
def login():
	pass

@user_bp.route('/logout')
def logout():
	pass

@user_bp.route('/info')
def info():
	pass

