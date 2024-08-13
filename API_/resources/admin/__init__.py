def get_function_name(func):
    def wrapper(*args, **kwargs):
        print(f"Function name: {func.__qualname__}")
        return func(*args, **kwargs)
    return wrapper