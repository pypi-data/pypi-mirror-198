from flask import request
from functools import wraps


def Controller():
    def wrapper(controllerClass):
        return NestController(
            controllerClass=controllerClass,
        )
    return wrapper


class NestController:
    lastController = None

    def __init__(self, controllerClass):
        self.name = controllerClass.__name__
        self.controllerClass = controllerClass
        self.controller = controllerClass

    def initController(self, context):
        routeNames = [name for name in dir(self.controller) if type(
            getattr(self.controller, name)).__name__ == 'NestRoute']
        for routeName in routeNames:
            route = getattr(self.controller, routeName)
            route.initRoute(context)


def Get(path):
    print(f"get defined {path}")

    def wrapper(func):
        return NestRoute(path=path, method='GET', callback=func)
        # print(f"get wrapper {path}")
        # def wrapped(*args, **kwargs):
        #    return func(*args, **kwargs)
        # return wrapped
    return wrapper


def Post(path):
    print(f"post defined {path}")

    def wrapper(func):
        return NestRoute(path=path, method='POST', callback=func)
        # print(f"post wrapper {path}")
        # def wrapped(*args, **kwargs):
        #    return func(*args, **kwargs)
        # return wrapped
    return wrapper


class NestRoute:
    def __init__(self, path, method, callback):
        self.callback = callback
        self.path = self.nestjsToFlaskPath(path)
        self.method = method

    def initRoute(self, context):
        print(f"init route {self.path}")
        app = context.get('app')
        app.add_url_rule(
            self.path,
            methods=[self.method],
            view_func=NestRoute.callbackWrapper(self.callback),
        )

    @staticmethod
    def callbackWrapper(callback):
        @wraps(callback)
        def wrapped(*args, **kwargs):
            return callback(NestRequest(request))
        return wrapped

    # Flask routing is different than NestJS routing
    def nestjsToFlaskPath(self, path: str) -> str:
        result = ''
        parts = path.split('/')
        for part in parts:
            if part.startswith(':'):
                result += '/<' + part[1:] + '>'
            else:
                result += '/' + part
        return result[1:]


class NestRequest:
    def __init__(self, request):
        self.request = request
        self.params = NestRequestParams(self.request)
        self.query = {}
        self.body = request.get_json(silent=True, force=True)
        self.headers = {}


class NestRequestParams(object):
    def __init__(self, request):
        super(NestRequestParams, self).__init__()
        self.request = request

    def __getattribute__(self, __name: str):
        if __name == 'request':
            return super(NestRequestParams, self).__getattribute__(__name)
        else:
            return self.request.view_args[__name]
            # return self.request.args.get(__name, type=str)
