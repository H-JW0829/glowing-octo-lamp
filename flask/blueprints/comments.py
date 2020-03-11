from flask import jsonify, request,Blueprint #新增jsonify处理json格式数据，request获取ajax前端发送来的参数。
from flask import json,Response
from exts import db
from model import Author,Blog,Comment
import myutils
comments_bp = Blueprint('comments',__name__)
@comments_bp.route('/submitComment', methods=('GET', 'POST'))
def submitComment():
    data = request.get_json()
    userName = data['user'].split(':')[1][1:-2]
    blogId = data['blogId']
    blog = Blog.query.filter(Blog.id == blogId).first()
    comment = data['comment']
    author = Author.query.filter(Author.user_name == userName).first()
    authorId = author.id
    id = myutils.createRandomString(10)
    try:
        comment = Comment(id=id,author=author,content=comment,blogId=blogId,authorId=authorId,blog=blog)
        db.session.add(comment)
        db.session.commit()
    except:
        db.session.rollback()
    try:
        comments = Comment.query.filter(Comment.blogId == blogId).order_by(-Comment.create_time).all()
        comments = myutils.to_json(comments)
        return_comments = []
        for i in range(len(comments)):
            temp = {}
            author = Author.query.filter(Author.id == comments[i]['authorId']).first()
            name = author.user_name
            temp['authorName'] = name
            temp['createTime'] = comments[i]['create_time']
            temp['content'] = comments[i]['content']
            return_comments.append(temp)
        state = {"status": "200", "msg": "成功拿到评论啦~"}
        return_comments.insert(0, state)
        return Response(json.dumps(return_comments), mimetype='application/json')
    except:
        return jsonify({"status": "400", "msg": "获取评论数据发生异常~"})

@comments_bp.route('/get_comments', methods=('GET', 'POST'))
def get_comments(id=None):
    try:
        blogId = request.args.get('id')
        comments = Comment.query.filter(Comment.blogId == blogId).order_by(-Comment.create_time).all()
        comments = myutils.to_json(comments)
        # print(comments)
        return_comments = []
        for i in range(len(comments)):
            temp = {}
            author = Author.query.filter(Author.id == comments[i]['authorId']).first()
            name = author.user_name
            temp['authorName'] = name
            temp['createTime'] = comments[i]['create_time']
            temp['content'] = comments[i]['content']
            return_comments.append(temp)
        state = {"status": "200", "msg": "成功拿到评论啦~"}
        return_comments.insert(0, state)
        return Response(json.dumps(return_comments),mimetype='application/json')
    except:
        return jsonify({"status": "400", "msg": "获取评论数据发生异常~"})