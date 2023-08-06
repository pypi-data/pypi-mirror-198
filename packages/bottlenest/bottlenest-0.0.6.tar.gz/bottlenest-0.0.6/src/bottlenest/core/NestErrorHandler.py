import traceback
from bottlenest.errors.http.HttpError import HttpError


class NestErrorHandler:
    def __init__(self, app, logger):
        self.app = app
        self.logger = logger

        self.init()

    def init(self):
        @self.app.errorhandler(Exception)
        def defaultErrorHandler(e):
            self.logger.log(
                'NestApplicationContext handle_exception', e, traceback.format_exc())
            # check if e is an instance of HttpError
            if isinstance(e, HttpError):
                return e.toDict(), e.statusCode
            return {"messages": [e.__str__()]}, 500
