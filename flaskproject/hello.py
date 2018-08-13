from flask import Flask, render_template, request, make_response
from flask import abort, redirect, url_for
from werkzeug import secure_filename

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    username = request.cookies.get('username')
    print("username->{}".format(username))
    # 注意这里引用cookies字典的键值对是使用cookies.get(key)
    # 而不是cookies[key]，这是防止该字典不存在时报错"keyerror"
    resp = make_response(render_template('hello.html', name=username))
    resp.set_cookie('username', 'Python')

    # 此处已经体现了  获取在视图中得到的响应对象 然后对响应对象设置不同的值  进而对返回对象进行修改 最终返回
    return resp


@app.route('/uploadfile')
def uploadfilePage():
    return render_template('uploadfile.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['testfile']
        f.save('upload/' + secure_filename(f.filename))
    return render_template('hello.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return render_template('hello.html', name=request.form['username'])
        else:
            error = 'Invalid username/password'
    else:
        error = 'Invalid request Type'
    # 当请求形式为“GET”或者认证失败则执行以下代码
    return render_template('login.html', error=error)


def valid_login(username, password):
    if "admin" == username and "admin" == password:
        return True
    else:
        return False


# @app.route('/<username>')
# def name(username):
#     return "Your name is " + username


@app.route('/sum/<int:num1>/<int:num2>')
def sum(num1, num2):
    return "sum is " + str(num1 + num2);


@app.route('/index')
def index():
    return redirect(url_for('login'))


@app.route('/abc')
def abc():
    abort(401)
    this_is_never_executed()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()