from functools import wraps


def type_valid(funck_check):
    def qube_func(func):
        @wraps(func)
        def tag_wrapper(*args, **kwargs):
            qube_res_dict = {}
            if args:
                args_tup = args
                for i in range(0, len(args_tup)):
                    try:
                        if funck_check(args_tup[i]):
                            qube_res = func(int(args_tup[i]))
                            type_arg = type(args_tup[i])
                            qube_res_dict.update({qube_res: type_arg})
                        else:
                            raise ValueError
                    except ValueError:
                        print(f'Некорректный формат числа {args_tup[i]} для возведения в куб.')
                        continue

            for key, value in kwargs.items():
                args_val = value
                try:
                    if funck_check(args_val):
                        qube_res_kw = func(int(args_val))
                        type_arg_kw = type(args_val)
                        qube_res_dict.update({qube_res_kw: type_arg_kw})
                    else:
                        raise ValueError
                except ValueError:
                    print(f'Некорректный формат числа {args_val} для возведения в куб.')
                    continue
            return f'Имя функции: {func.__name__}, аргументы {args, kwargs},  результат функции: {qube_res_dict}'

        return tag_wrapper

    return qube_func


@type_valid(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(25, 6, n=5, m=13))
print(calc_cube(-15))
