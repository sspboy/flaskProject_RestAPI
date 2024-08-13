# 登录验证

# 登录成功：：获取用户配置信息

# 登录失败

# 获取权限：：配置全局用户信息

# 功能权限验证模块


class Login():
    def __init__(self):
        pass

    def get_user_message(self):
        pass


def get_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__qualname__}")
        return func(*args, **kwargs)
    return wrapper


