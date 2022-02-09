from functools import wraps


def qube_func(func):
    @wraps(func)
    def tag_wrapper(*args, **kwargs):
        qube_res_dict = {}
        for key, value in kwargs.items():
            args_val = value
            qube_res_kw = func(int(args_val))
            type_arg_kw = type(args_val)
            qube_res_dict.update({qube_res_kw: type_arg_kw})
        if args:
            args_tup = args
            for i in range(0, len(args_tup)):
                qube_res = func(int(args_tup[i]))
                type_arg = type(args_tup[i])
                qube_res_dict.update({qube_res: type_arg})
        return f'Имя функции: {func.__name__}, аргументы {args, kwargs},  результат функции: {qube_res_dict}'

    return tag_wrapper


@qube_func
def calc_cube(x):
    return x ** 3


print(calc_cube(15, 6, n=5, m=13))
print(calc_cube(109, 55))
