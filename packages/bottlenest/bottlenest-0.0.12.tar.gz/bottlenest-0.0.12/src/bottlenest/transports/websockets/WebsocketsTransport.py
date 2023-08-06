from .factories.WebsocketsFactory import WebsocketsFactory


class WebsocketsTransport:
    # called by user, passing any options
    def __init__(self):
        pass

    def setupTransport(self, appContext, moduleContext):
        print("================== setup WebsocketsTransport")
        # self.appContext = appContext
        # self.module = appContext.module
        # self.logger = appContext.logger
        WebsocketsFactory.setAppContext(appContext)
        pass

    def listen(self, callback):
        WebsocketsFactory.listen()
        callback()

    # def listen(self, callback):
    #     # TODO: review this port to allow multiple ports
    #     port = self.appContext.get('port')
    #     app = self.appContext.get('app')
    #     eventlet.wsgi.server(eventlet.listen(('', port)), app)
    #     callback()
