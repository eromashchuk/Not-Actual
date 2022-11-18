def my_decorator(fn):
    print("Этот код будет выведен один раз в момент декорирования функции")
    def wrapper(*args, **kwargs):
        print('Этот код будет выполняться перед каждым вызовом функции')
        result = fn(*args, **kwargs)
        print('Этот код будет выполняться после каждого вызова функции')
        return result
    return wrapper

@my_decorator
def tyu(n, x):
    print(pow(n, x))

@my_decorator
def tre(str_):
    print(str_)

tyu(20,5)
tyu(5, 5)
tre("fdf")