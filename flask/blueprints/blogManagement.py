from flask import jsonify, request ,Blueprint,Response,json
from exts import db
from model import Author,Blog
import myutils
bm_bp = Blueprint('bm',__name__)
@bm_bp.route('/delete_blog', methods=('GET', 'POST'))
def delete_blog():
    try:
        id = request.args.get('id')
        blog = Blog.query.filter(Blog.id == id).first()
        db.session.delete(blog)
        db.session.commit()
        return jsonify({'status':'200','msg':'删除博客成功啦~'})
    except:
        return jsonify({"status":"400", "msg": "删除博客失败~"})

@bm_bp.route('/edit_blog', methods=('GET', 'POST'))
def edit_blog():
    try:
        data = request.get_json()
        title = data['title']
        content = data['content']
        categories = "-".join(data['category'])
        name = data['author']
        author = Author.query.filter(Author.user_name == name).first()
        authorId = author.id
        id = data['id']
        blog = Blog.query.filter(Blog.id == id).first()
        blog.title = title
        blog.content = content
        blog.category = categories
        blog.authorId = authorId
        db.session.commit()
        return jsonify({'status':'200','msg':'编辑成功啦~'})
    except:
        return jsonify({"status":"400", "msg": "编辑发生异常~"})

@bm_bp.route('/add_blog', methods=('GET', 'POST'))
def add_blog():
    data = request.get_json()
    title = data['title']
    content = data['content']
    categories = "-".join(data['categories'])
    name = data['author']
    author = Author.query.filter(Author.user_name == name).first()
    authorId = author.id
    id = myutils.createRandomString(10)
    try:
        blog = Blog(id=id,authorId=authorId,content=content,category=categories,title=title,author=author)
        db.session.add(blog)
        db.session.commit()
        return jsonify({"status":"200","msg":"哈哈，添加博客成功啦~"})
    except:
        db.session.rollback()
        return jsonify({"status":"400","msg":"哎呀，添加博客异常，请您确保输入的信息无误~"}) #返回一个json格式的数据

@bm_bp.route('/collectBlog', methods=('GET', 'POST'))
def collectBlog():
    data = request.get_json()
    userName = data['user'].split(':')[1][1:-2]
    author = Author.query.filter(Author.user_name == userName).first()
    blogId = data['blogId']
    try:
        if author.favoriteBlogs:
            if blogId not in author.favoriteBlogs:
                author.favoriteBlogs += ('|' + blogId)
        else:
            author.favoriteBlogs = blogId
        db.session.commit()
        state = {"status": "200", "msg": "成功从数据库拿到数据~"}
        return Response(json.dumps(state),mimetype='application/json')
    except:
        return jsonify({"status": "400", "msg": "获取数据发生异常~"})