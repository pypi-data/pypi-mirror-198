from bottlenest.metaClasses.NestProvider import NestProvider
from .NestSubscribeMessage import NestSubscribeMessage
from ..factories.WebsocketsFactory import WebsocketsFactory

servers = []


class NestWebSocketGateway(NestProvider):
    __name__ = 'NestWebSocketGateway'

    def __init__(self, cls, port=4001, namespace=None):
        self.cls = cls
        self.providerName = cls.__name__
        self.port = port
        self.namespace = namespace

    def getName(self):
        return self.cls.__name__

    def eventName(self):
        return NestSubscribeMessage.__name__

    # called from whithin the module's setup
    def setupProvider(self, module, context):
        print(f"NestSocketGateway setupProvider {self.providerName}")
        self.module = module
        self.context = context
        # get sio from WebsocketsTransport
        WebsocketsFactory.registerGateway(self, context)
        self._setupProvider(module, context)

    def listen(self):
        print(f"NestSocketGateway listen {self.providerName}")
