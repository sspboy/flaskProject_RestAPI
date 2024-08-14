from flask import Flask
from API_.resources.admin.BluePrintAdmin import admin_blueprint
from API_.resources.BasicSettings.BluePrintBasicSettings import setting_blueprint

app = Flask(__name__)

# 登录


# admin管理后台
app.register_blueprint(admin_blueprint, url_prefix='/admin')


# 前台应用-我的设置
app.register_blueprint(setting_blueprint, url_prefix='/setting')


# 前台应用-appname


if __name__ == '__main__':

    app.run(debug=True)