def Param(name):
    def wrapper(variable):
        return name
    return wrapper
