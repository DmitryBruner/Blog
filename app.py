from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from model import Post, Users
from config import *
#from forms import LoginForm
from flask_login import login_required

@login_required
@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


@app.route('/post/<int:id_post>', methods=['POST', 'GET'])
def post(id_post):
    post = Post.query.all()[id_post]
    return render_template('post.html', post=post)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'При добавлении статьи произошла ошибка'
    else:
        return render_template('create.html')


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/login', method=['POST'])
def login():
    if request.method == 'POST':

    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['moypar'])
        if len(request.form['name']) > 4 and len(request.form['email']) > 4 and len(request.form['moypar']) > 4 and \
                request.form['moypar'] == request.form['repeat_moypar']:
            name = request.form['name']
            email = request.form['email']
            hash_psw = generate_password_hash(request.form['moypar'])
            user = Users(name=name, email=email, password=hash_psw)
            print(name, hash_psw, email)
            try:
                db.session.add(user)
                db.session.commit()
                return 'done'  # redirect(url_for('login'))
            except:
                return 'Ошибка при регистрации'
    else:
        return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
