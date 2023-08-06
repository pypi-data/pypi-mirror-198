from bottlenest.transports.websockets.decorators.NestWebSocketGateway import NestWebSocketGateway
from bottlenest.transports.websockets.decorators.NestSubscribeMessage import NestSubscribeMessage

# música boa
# https://www.youtube.com/watch?v=KCwk1qeh0gM
# https://www.youtube.com/watch?v=Xj4ETM2IJY8&list=PLTeMoz1bBorZjs92TBazC_QSvGOfw-CJS&index=7


def WebSocketGateway(port=80, namespace=None):
    def wrapper(gatewayClass):
        return NestWebSocketGateway(
            cls=gatewayClass,
            port=port,
            namespace=namespace,
        )
    return wrapper


def SubscribeMessage(eventName):
    def wrapper(messageClass):
        return NestSubscribeMessage(
            callback=messageClass,
            eventName=eventName,
        )
    return wrapper
