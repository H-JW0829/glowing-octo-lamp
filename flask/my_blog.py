from flask import Flask
from exts import db
import config

from blueprints.comments import comments_bp
from blueprints.blogManagement import bm_bp
from blueprints.getBlogs import getBlogs_bp
from blueprints.login import login_bp

app = Flask(__name__)
app.register_blueprint(comments_bp)
app.register_blueprint(bm_bp)
app.register_blueprint(getBlogs_bp)
app.register_blueprint(login_bp)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
  return "hhh"

if __name__ == '__main__':
    app.run()