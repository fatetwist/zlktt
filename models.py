
from exts import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User', backref='role')

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, unique=True, primary_key=True,autoincrement=True)
    username = db.Column(db.String(24), unique=True, index=True, nullable=False)
    phone_num = db.Column(db.Integer,unique=True, nullable=False)
    password = db.Column(db.String(18), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %s>' % self.username

class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    time = db.Column(db.String(),nullable=False)
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    author = db.relationship('User', backref=db.backref('articles'))
    tags = db.relationship('Tag', secondary='article_tag',backref='articles')
    def __repr__(self):
        return '<Article %s|%s>' % (self.title, self.author.username)

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64),unique=True)
    def __repr__(self):
        return '<Tag %s>' % self.name

article_tag = db.Table('article_tag',
         db.Column('article_id', db.Integer, db.ForeignKey('articles.id'), primary_key=True),
         db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True))