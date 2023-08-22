"""
Decorators are one of the most helpful and powerful tools of Python. These are used to modify the behavior of the function.
Decorators provide the flexibility to wrap another function to expand the working of wrapped function, without permanently modifying it.

"""
# def deco_func(myfunc):
#     def wrapp():
#         print("before")
#         myfunc()
#         print("after")
#     return wrapp
# @deco_func
# def myfunc():
#     print("inside")
#
# myfunc()

# def decorat(fun):
#     def inner():
#         print("inner")
#         fun()
#     return inner
# @decorat
# def test():
#     print("decorated")
#
# test()


# def upper_decor(fun):
#     def wrapper(name):
#         result=fun(name)
#         return result.upper()
#     return wrapper
# @upper_decor
# def hello(name):
#     return "hello"+name
#
# print(hello("karthik"))




