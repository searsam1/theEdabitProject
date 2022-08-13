def every_some(test, val, *args):

    if val == "everybody":
        return all(eval("{} {}".format(i,test)) for i in args)
    return any(eval("{} {}".format(i,test)) for i in args)

