from flask import request
from functools import wraps
from bottlenest.metaClasses.NestProvider import NestProvider
from bottlenest.transports.http.decorators.NestRoute import NestRoute

# TODO: add support for route prefix


class NestController(NestProvider):
    __name__ = 'NestController'

    def eventName(self):
        return NestRoute.__name__
