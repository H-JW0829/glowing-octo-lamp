from flask import jsonify, request ,Blueprint
from exts import db
from model import Author
import myutils
login_bp = Blueprint('login',__name__)
@login_bp.route('/login', methods=('GET', 'POST'))
def login():
    # try:
    data = request.get_json()
    print(data)
    username = data['username']
    password = data['password']
    author = Author.query.filter(Author.user_name == username).first()
    if author:
        if author.password == password:
            return jsonify({'status':'0','msg':'登录成功~'})
        else:
            return jsonify({'status':'1','msg':'密码输入错误~'})
    else:
        return jsonify({'status':'2','msg':'该用户不存在~'})

@login_bp.route('/regist', methods=('GET', 'POST'))
def regist():
    # try:
    data = request.get_json()
    print(data)
    username = data['newUsername']
    password = data['newPassword']
    user = Author.query.filter(Author.user_name == username).first()
    if user:
        return jsonify({'status':'1','msg':'该用户名已存在，请重新输入~'})
    else:
        try:
            id = myutils.createRandomString(10)
            user = Author(user_name=username, password=password,id=id)
            db.session.add(user)
            db.session.commit()
            return jsonify({'status': '0', 'msg': '注册成功~'})
        except:
            db.session.rollback()
            return jsonify({'status':'2','msg':'系统异常，请稍后再试或联系管理员~'})