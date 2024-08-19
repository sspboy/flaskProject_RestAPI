from flask import Flask,request,session
from API_.resources.admin.BluePrintAdmin import admin_blueprint
from API_.resources.BasicSettings.BluePrintBasicSettings import setting_blueprint
from API_.resources.Login.BluePrintLogin import login_blueprint
import datetime

# 初始化login-login库
from API_.resources.Login.Model_Login import login_manager

app = Flask(__name__)
app.secret_key = 'sspboy'                           # Change this!
app.permanent_session_lifetime = datetime.timedelta(minutes=100)  # 1分钟有效的seassion
login_manager.init_app(app)

# login 登录模块
app.register_blueprint(login_blueprint, url_prefix='/login')


# admin管理后台
app.register_blueprint(admin_blueprint, url_prefix='/admin')


# 前台应用-我的设置
app.register_blueprint(setting_blueprint, url_prefix='/setting')


# 前台应用-appname


if __name__ == '__main__':

    app.run(port=5000,debug=True,host='0.0.0.0')