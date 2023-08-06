class NestSubscribeMessage:
    def __init__(self, callback, eventName):
        self.eventName = eventName
        self.callback = callback

    def setup(self, cls, context):
        print(f"setup event {self.eventName}")
        sio = context.get('sio')

        @sio.on(self.eventName)
        def _callback(sid, data):
            print(f"NestSubscribeMessage {self.eventName}")
            result = self.callback(cls, data)
            if result is not None:
                sio.emit(self.eventName, result, room=sid)
