from flask import Flask
from bottlenest.transports.http.errors import HttpError
import traceback


class HttpTransport:
    def __init__(self, port=3500):
        self.port = port

    def setup(self, context):
        self.context = context
        self.module = self.context.get('module')
        self.logger = self.context.get('logger')
        self.app = Flask(self.module.name)
        self.context.set('app', self.app)
        self.setupErrorHandlers()

    def setupErrorHandlers(self):
        @self.app.errorhandler(Exception)
        def defaultErrorHandler(e):
            self.logger.log(
                'NestApplicationContext handle_exception', e, traceback.format_exc())
            # check if e is an instance of HttpError
            if isinstance(e, HttpError):
                return e.toDict(), e.statusCode
            return {"messages": [e.__str__()]}, 500

    def listen(self, callback):
        self.app.run(port=self.port, debug=True)
        callback()
