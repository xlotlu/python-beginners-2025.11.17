def myfunc(arg1, arg2, kwarg1="default", kwarg2="another default"):
    print("  arg1 :", arg1)
    print("  arg2 :", arg2)
    print("kwarg1 :", kwarg1)
    print("kwarg2 :", kwarg2)

"""
myfunc(1, 2)
myfunc(1, 2, 3)
myfunc(kwarg2=1, kwarg1=2, arg2=4, arg1=18)
myfunc(4, 18, kwarg2=1, kwarg1=2)
"""

def myfunc_gen_args(arg1, arg2, *args):
    print("  arg1 :", arg1)
    print("  arg2 :", arg2)
    print("  args :", args)


def myfunc_gen_kwargs(kwarg1="default", **kwargs):
    print("  kwarg1 :", kwarg1)
    print("  kwargs :", kwargs)


def myfunc_gen_everything(arg1, arg2, *args, kwarg1=None, **kwargs):
    print("  arg1 :", arg1)
    print("  arg2 :", arg2)
    print("  args :", args)

    print("  kwarg1 :", kwarg1)
    print("  kwargs :", kwargs)

# mai există
# delimitatorii speciali:
#    *
# și
#    /
