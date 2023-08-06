from flask import request
from functools import wraps
from bottlenest.transports.http.decorators.NestRequest import NestRequest


class NestRoute:
    __name__ = 'NestRoute'

    def __init__(self, path, method, callback):
        print(f"route defined {method} {path}")
        self.callback = callback
        self.path = self._nestjsToFlaskPath(path)
        self.method = method

    def setup(self, cls, context):
        print(f"init route {self.path}")
        app = context.get('app')
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
