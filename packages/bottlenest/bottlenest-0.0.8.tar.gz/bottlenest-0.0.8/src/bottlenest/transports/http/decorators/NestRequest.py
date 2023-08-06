class NestRequest:
    def __init__(self, request):
        self.request = request
        self.params = NestRequestParams(self.request)
        self.query = {}
        self.body = request.get_json(silent=True, force=True)
        self.headers = {}

        if self.body is None:
            self.body = {}


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
