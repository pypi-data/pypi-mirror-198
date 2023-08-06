class NestLogger:
    def __init__(self):
        self.context = None
        # self.log('NestLogger initialized')

    def setContext(self, context):
        self.context = context
        # self.log('NestLogger context set')

    def log(self, *args):
        print(*args)
