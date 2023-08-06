from bottlenest.transports.http.decorators.NestHttpModule import NestHttpModule
from bottlenest.transports.http.decorators.NestController import NestController
from bottlenest.transports.http.decorators.NestRoute import NestRoute


# TODO: Use metaclasses https://www.youtube.com/watch?v=yWzMiaqnpkI
# 14:11


def Module(controllers=[], imports=[], providers=[]):
    def wrapper(moduleClass):
        return NestHttpModule(
            moduleClass=moduleClass,
            imports=imports,
            controllers=controllers,
            providers=providers,
        )
    return wrapper


def Controller():
    def wrapper(controllerClass):
        return NestController(
            cls=controllerClass,
        )
    return wrapper


def Get(path):
    print(f"get defined {path}")

    def wrapper(func):
        return NestRoute(
            callback=func,
            path=path,
            method='GET',
        )
    return wrapper


def Post(path):
    print(f"post defined {path}")

    def wrapper(func):
        return NestRoute(
            callback=func,
            path=path,
            method='POST',
        )
    return wrapper
