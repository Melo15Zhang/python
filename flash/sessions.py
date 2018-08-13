from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = 'wing1995 is a very good girl'


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return render_template('main.html', username=username)
        else:
            return render_template('fault.html')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    # 如果用户名存在，则从会话中移除该用户名
    session.pop('username', None)
    return render_template('login.html')


# 设置密钥，保证会话安全
if __name__ == "__main__":
    app.run()