from flask import Flask,redirect,request,session
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ''
app.config['SECRET_KEY'] = "lkkajdghdadkglajkgah"

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
  def __init__(self,id):
    self.id = id


@app.route('/')
def home():
    return "home: <a href='/login/'>Login</a> <a href='/protected/'>Protected</a> <a href='/logout/'>Logout</a>"

@app.route('/protected/')
@login_required
def protected():
    return "protected "+current_user.get_id()

@app.route('/login/')
def login():
    login_user(User(1))
    return "you are logged in"

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return "you are logged out"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=1212,debug=True)
