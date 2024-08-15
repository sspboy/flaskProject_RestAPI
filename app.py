from flask import Flask,request,session
from API_.resources.admin.BluePrintAdmin import admin_blueprint
from API_.resources.BasicSettings.BluePrintBasicSettings import setting_blueprint
import datetime
# 初始化login-login库
from flask_login import LoginManager, login_user, logout_user, login_required,current_user
from API_.resources.Login.Model_Login import User,LoadingUser

app = Flask(__name__)
app.secret_key = 'sspboy'                           # Change this!
app.permanent_session_lifetime = datetime.timedelta(minutes=100)  # 1分钟有效的seassion


login_manager = LoginManager()                      # 初始化一个 LoginManager 类对象
login_manager.login_message_category = 'info'       # 消息类别，默认是 ‘message’
login_manager.login_message = 'Access denied.'      # 用户未登录时显示的消息；
login_manager.session_protection = "strong"
login_manager.init_app(app)

# 登录

@login_manager.user_loader
def user_loader(username):

    load = LoadingUser(username)

    # 从数据库或 读取用户信息
    user_obj = load.get_user_obj()

    if user_obj == 'None':  # 用户名为空，用户不存在

        return 'None'

    elif user_obj != 'None':  # 存户名不为空，用户存在

        id = user_obj.get('id')  # 用户对象定义id

        username = user_obj.get('nickname')  # 用户对象定义品牌-id

        pass_word = user_obj.get('pass_word')  # 用户对象-定义密码

        role = ['admin']  # 用户对象-定义角色

        menu = ''  # 菜单权限

        # 个人、部门、全公司
        data_permission = ''  # 数据权限

        user = User(id,username,pass_word)

        return user


@app.route('/login',methods=['POST'])
def login():

    if request.method == 'POST':

        u_data= request.get_json()

        user_name= u_data.get('username') # 前台提交的用户

        pass_word = u_data.get('password') # 前台提交的密码

        user_obj = user_loader(user_name)   # 数据库查询获取的用户信息

        if user_obj == 'None':              # 用户不存在

            return 'None'
        # 密码 用户名称 正确 登录成功
        elif user_obj.password == pass_word and user_obj.id == user_name:

            login_user(user_obj)

            session.permanent = True                                          # 记住用户

            app.permanent_session_lifetime = datetime.timedelta(minutes=100)    # 1分钟有效的seassion

            return 'true'

        else:   #密码 用户名不正确 登录失败

            return 'false'


# 退出登录
@app.route('/logout')
@login_required
def logout():
    logout_user()
    # return render_template('/view/login.html')
    return 'login out True'


# 未登录授权的提示页面
@login_manager.unauthorized_handler
def unauthorized():
    return 'NO power'



# admin管理后台
app.register_blueprint(admin_blueprint, url_prefix='/admin')


# 前台应用-我的设置
app.register_blueprint(setting_blueprint, url_prefix='/setting')


# 前台应用-appname123


if __name__ == '__main__':

    app.run(debug=True)