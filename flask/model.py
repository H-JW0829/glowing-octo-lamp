from exts import db
from datetime import datetime
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.String(30),primary_key=True)
    user_name = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    favoriteBlogs = db.Column(db.String(5000))

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.String(30),primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    category = db.Column(db.String(50),nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    authorId = db.Column(db.String(30), db.ForeignKey('author.id'))
    author = db.relationship('Author', backref=db.backref('blogs'))


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.String(30),primary_key=True)
    create_time = db.Column(db.DateTime,default=datetime.now)
    content = db.Column(db.Text,nullable=False)  #db.Text表示不固定长度的字符串
    blogId = db.Column(db.String(30),db.ForeignKey('blog.id'))
    authorId = db.Column(db.String(30),db.ForeignKey('author.id'))

    blog = db.relationship('Blog',backref=db.backref('comments'))
    author = db.relationship('Author',backref=db.backref('comments'))