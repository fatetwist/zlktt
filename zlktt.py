from flask import Flask,request,render_template,session
import config
app = Flask(__name__)
app.config.from_object(config)
from models import User, Tag, Article, Role
from exts import db

db.init_app(app)

@app.before_request
def before():
    session.permanent = True


# with app.app_context():
#     role = Role.query.filter(Role.name=='visitor').first()
#     # # users = User.query.all()
#     # # for x in users:
#     # #     x.role = role
#     # user = User(username = 'licong', password='123456', phone_num='14770807181',role=role)
#     # db.session.add(user)
#     # db.session.commit()
#     user = User.query.all()
#     for x in user:
#         x.role = role
#
#     db.session.commit()


# title='最美的世界'
# content = '我喜欢你啊'
# time = '2017-11-18 13:35:06'
# article = Article(title=title,content=content,time=time,author_id=1)
# print('已完成创建')
# db.session.add(article)
# db.session.commit()
# print('创建完毕')

def Isphone(string):

    length = len(string)
    if length != 11 and string.isdigit() is not True:
        return False
    else:
        return True


def Islogin():
    if session.get('username') == None:
        return False
    else:
        username = session.get('username')
        password = session.get('password')
        user = User.query.filter(User.username==username).first()
        if user.password == password:
            return True
        else:
            return False




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if Isphone(username):
            user = User.query.filter(User.phone_num==username).first()
            if user is not None and password == user.password:
                session['username'] = user.username
                session['password'] = password
                return '通过手机号登录成功'
        else:
            user = User.query.filter(User.username==username).first()
            if user is not None and user.password==password:
                session['username'] = user.username
                session['password'] = password
                return '通过用户名登录成功！'
        return '账号或密码错误'
    else:
        return render_template('login.html')
@app.route('/search/', methods=['GET'])
def search():
    key_tag = request.args.get('key_tag')

    if key_tag != None:

        tag_res = Tag.query.filter(Tag.name == key_tag).first()
        if tag_res != None:
            articles = tag_res.articles
            return render_template('search.html', articles=articles)
        else:
            return render_template('search.html', Noneres=True)

    else:
        return render_template('search.html')





@app.route('/regist/', methods=['GET','POST'])
def regist():
    if request.method=='GET':
        return render_template('regist.html')
    else:
        username = request.form['username']
        password = request.form['password']
        phone_num = request.form['phone_num']
        print('正在创建')
        user=User(username=username,password=password,phone_num=phone_num)
        print('创建成功！')
        db.session.add(user)
        db.session.commit()
        return '注册成功！'

@app.route('/raiseq/',methods=['GET','POST'])
def raiseq():
    if Islogin() == False:
        return '未登录或身份已经过期'
    if request.method =='GET':
        return render_template('raiseq.html')
    else:
        tags1 = request.form.get('tags')
        tags2 = tags1.split(',')
        time = '2017-11-18 13:14:17'
        title = request.form.get('title')
        content = request.form.get('content')
        article = Article(author_id=user.id, time=time, title=title, content=content)
        for x in tags2:
            tag_a = Tag.query.filter(Tag.name==x).first()
            if tag_a is not None:
                article.tags.append(tag_a)
            else:
                tag = Tag(name=x)
                article.tags.append(tag)
                db.session.add(tag)
        db.session.add(article)
        db.session.commit()
        return '提交成功！'
@app.route('/content/')
def content():
    if Islogin() == False:
        return '未登录或身份已经过期'
    articles = Article.query.all()
    return render_template('content.html',articles=articles)

if __name__ == '__main__':
    app.run()
