from ..NestHttpModule import NestHttpModule
from .NestController import NestController
from .NestRoute import NestRoute


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


def Put(path):
    print(f"put defined {path}")

    def wrapper(func):
        return NestRoute(
            callback=func,
            path=path,
            method='PUT',
        )
    return wrapper


def Delete(path):
    print(f"delete defined {path}")

    def wrapper(func):
        return NestRoute(
            callback=func,
            path=path,
            method='DELETE',
        )
    return wrapper


def Patch(path):
    print(f"patch defined {path}")

    def wrapper(func):
        return NestRoute(
            callback=func,
            path=path,
            method='PATCH',
        )
    return wrapper
