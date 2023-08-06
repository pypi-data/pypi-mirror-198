from flask import request
from functools import wraps


class NestRoute:
    __name__ = 'NestRoute'

    def __init__(self, path, method, callback):
        print(f"route defined {method} {path}")
        self.callback = callback
        self.path = self._nestjsToFlaskPath(path)
        self.method = method

    def setupEvent(self, cls, moduleContext):
        print(f"NestRoute setupEvent {self.path}")
        print(moduleContext)
        transport = moduleContext.get('transport')
        app = transport.app
        # app = moduleContext.get('app')
        app.add_url_rule(
            self.path,
            methods=[self.method],
            view_func=self._callbackWrapper(cls),
        )

    def _callbackWrapper(self, cls):
        @wraps(self.callback)
        def wrapped(*args, **kwargs):
            return self.callback(cls, NestRequest(request))
            # return self.callback(context)
        return wrapped

    # Flask routing is different than NestJS routing
    def _nestjsToFlaskPath(self, path: str) -> str:
        result = ''
        parts = path.split('/')
        for part in parts:
            if part.startswith(':'):
                result += '/<' + part[1:] + '>'
            else:
                result += '/' + part
        return result[1:]

##################################################################


class NestRequest:
    __name__ = 'NestRequest'

    def __init__(self, request):
        self.request = request
        self.params = NestRequestParams(self.request)
        self.query = {}
        self.body = request.get_json(silent=True, force=True)
        self.headers = {}

        if self.body is None:
            self.body = {}


class NestRequestParams(object):
    __name__ = 'NestRequestParams'

    def __init__(self, request):
        super(NestRequestParams, self).__init__()
        self.request = request

    def __getattribute__(self, __name: str):
        if __name == 'request':
            return super(NestRequestParams, self).__getattribute__(__name)
        else:
            return self.request.view_args[__name]
            # return self.request.args.get(__name, type=str)
