import eventlet
import socketio
from bottlenest.metaClasses.NestProvider import NestProvider
from bottlenest.transports.websockets.decorators.NestSubscribeMessage import NestSubscribeMessage


class NestWebSocketGateway(NestProvider):
    __name__ = 'NestWebSocketGateway'

    def __init__(self, cls, port=4001, namespace=None):
        self.cls = cls
        self.port = port
        self.namespace = namespace

    def eventName(self):
        return NestSubscribeMessage.__name__

    def setup(self, module, context):
        self.module = module
        self.context = context
        sio = context.get('sio')
        context.set('port', self.port)

        def _onConnect(sid, environ, auth):
            print(f"[NestWebsocketGateway] onConnect {sid}")

        sio.on('connect')(_onConnect)

        self._setup(module, context)
