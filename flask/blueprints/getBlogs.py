from flask import jsonify, request,Blueprint #新增jsonify处理json格式数据，request获取ajax前端发送来的参数。
from flask import json,Response
from exts import db
from model import Author,Blog
import myutils
getBlogs_bp = Blueprint('getBlogs',__name__)
@getBlogs_bp.route('/get_all_blogs', methods=('GET', 'POST'))
def get_all_blogs():
    try:
        sql = 'select * from Blog;'
        blogs = db.session.execute(sql)
        blogs = Blog.query.order_by(-Blog.create_time)
        blogs = myutils.to_json(blogs)
        state = {"status": "200", "msg": "成功从数据库拿到数据~"}
        blogs.insert(0,state)
        return Response(json.dumps(blogs),mimetype='application/json')
    except:
        return jsonify({"status": "400", "msg": "获取数据发生异常~"})

@getBlogs_bp.route('/get_single_blog', methods=('GET', 'POST'))
def get_single_blog():
    try:
        id = request.args.get('id')
        blog = Blog.query.filter(Blog.id == id)
        blog = myutils.to_json(blog)
        authorId = blog[0]['authorId']
        author = Author.query.filter(Author.id == authorId).first()
        blog[0]['author'] = author.user_name
        state = {"status": "200", "msg": "成功从数据库拿到数据~"}
        blog.insert(0, state)
        return Response(json.dumps(blog),mimetype='application/json')
    except:
        return jsonify({"status": "400", "msg": "获取数据发生异常~"})

@getBlogs_bp.route('/get_personal_blogs', methods=('GET', 'POST'))
def get_personal_blogs():
    data = request.get_json()
    userName = data['user'].split(':')[1][1:-2]
    author = Author.query.filter(Author.user_name == userName).first()
    authorId = author.id
    try:
        blogs = Blog.query.filter(Blog.authorId == authorId)
        blogs = myutils.to_json(blogs)
        blogs = myutils.sortBlogsByTime(blogs)
        state = {"status": "200", "msg": "成功从数据库拿到数据~"}
        blogs.insert(0,state)
        return Response(json.dumps(blogs),mimetype='application/json')
    except:
        return jsonify({"status": "400", "msg": "获取数据发生异常~"})

@getBlogs_bp.route('/get_favorite_blogs', methods=('GET', 'POST'))
def get_favorite_blogs():
    data = request.get_json()
    userName = data['user'].split(':')[1][1:-2]
    author = Author.query.filter(Author.user_name == userName).first()
    try:
        favoriteBlogs = []
        if '|' in author.favoriteBlogs:
            blogs = author.favoriteBlogs.split('|')
        else:
            blogs = [author.favoriteBlogs]
        for blogid in blogs:
            blog = Blog.query.filter(Blog.id == blogid)
            if blog:
                blog = myutils.to_json(blog)
                favoriteBlogs.extend(blog)
        favoriteBlogs = myutils.sortBlogsByTime(favoriteBlogs)
        state = {"status": "200", "msg": "成功从数据库拿到数据~"}
        favoriteBlogs.insert(0,state)
        return Response(json.dumps(favoriteBlogs),mimetype='application/json')
    except:
        return jsonify({"status": "400", "msg": "获取数据发生异常~"})



@getBlogs_bp.route('/get_authors', methods=('GET', 'POST'))
def getAuthors():
    try:
        sql = 'select * from Author;'
        authors = db.session.execute(sql)
        authors = Author.query.filter().all()
        authors = myutils.to_json(authors)
        state = {"status": "200", "msg": "成功从数据库拿到数据~"}
        authors.insert(0, state)
        print(authors)
        return Response(json.dumps(authors), mimetype='application/json')
    except:
        return jsonify({"status": "400", "msg": "获取数据发生异常~"})