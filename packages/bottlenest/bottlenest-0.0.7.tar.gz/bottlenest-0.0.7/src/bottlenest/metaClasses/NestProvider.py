from abc import ABC, abstractmethod, ABCMeta, abstractproperty
from bottlenest.metaClasses.NestProviderContext import NestProviderContext


class NestProvider(ABC):
    # def __call__(cls, *args, **kwargs):
    #    instance = super(NestProvider, cls).__call__(*args, **kwargs)
    #    # instance.setup(*args, **kwargs)
    #    return instance

    # @abstractmethod
    @property
    def name(self):
        return self.cls.__name__

    @property
    @abstractmethod
    def eventName(self):
        return 'NestEvent'

    def __init__(self, cls):
        self.cls = cls
        # self.name = cls.__name__

    def _getEventNames(self):
        eventClassName = self.eventName()
        eventNames = dir(self.provider)
        eventNames = [name for name in eventNames if type(
            getattr(self.provider, name)).__name__ == eventClassName]
        return eventNames

    def setup(self, module, context):
        self._setup(module, context)

    def _setup(self, module, context):
        print("thiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiis setup")
        self.module = module
        self.context = context
        eventContext = NestProviderContext(self)
        self.provider = self.cls(eventContext)
        eventNames = self._getEventNames()
        for eventName in eventNames:
            # print("---->> eventName: ", eventName)
            event = getattr(self.provider, eventName)
            event.setup(self.provider, context)
