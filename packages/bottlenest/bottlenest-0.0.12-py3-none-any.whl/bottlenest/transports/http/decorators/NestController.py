from bottlenest.metaClasses.NestProvider import NestProvider
from .NestRoute import NestRoute

# TODO: add support for route prefix


class NestController(NestProvider):
    __name__ = 'NestController'

    def eventName(self):
        return NestRoute.__name__
