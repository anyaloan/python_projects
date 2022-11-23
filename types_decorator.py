from functools import wraps

def types(*args, _ret):
    def callable1(myfunc):
        @wraps(myfunc)
        def check_it(*par):
            if args != tuple([type(el) for el in par]):
                raise Exception("Provide valid type")
            ret = myfunc(*par)
            if type(ret) != _ret:
                raise Exception("Not valid result type")
            return ret
        return check_it
    return callable1


@types(int, float, _ret=float)
def plus(a, b):
    return a + b


print(plus(7, 4.0))


@types(str, _ret=str)
def rev(txt):
    return txt[::-1]


print(rev("hello"))

@types(list, list, _ret=list)
def makelist(l1, l2):
    l1.append(l2)
    return tuple(l1)
