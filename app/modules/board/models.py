from app import db
from datetime import datetime
# from app.modules.user.models import User


class Board(db.Model):
    __tablename__ = 'board'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, index=True)


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)

    # Many(Posts) to one(Board)
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    board = db.relationship('Board')

    # Many(Posts) to one(User)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User')

    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=True)
    hit = db.Column(db.Integer, nullable=False, default=0)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)

    # Many(Comments) to one(Post)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    post = db.relationship('Post')

    # Many(Posts) to one(User)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User')

    content = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())