from bottlenest.core.NestContainer import NestContainer
from bottlenest.core.NestLogger import NestLogger
from bottlenest.core.NestErrorHandler import NestErrorHandler
from flask import Flask


class NestApplicationContext:
    def __init__(self, module, options):
        self.module = module
        self.options = options
        self.container = NestContainer()
        self.logger = NestLogger()
        self.logger.setContext(self)
        # self.logger.log('NestApplicationContext initialized')
        # self.logger.log('NestApplicationContext module: ' +
        #                 str(self.module.name))
        self.logger.log('NestApplicationContext options: ' + str(self.options))
        # self.logger.log('NestApplicationContext container: ' +
        #                str(self.container))
        # self.logger.log('NestApplicationContext logger: ' + str(self.logger))
        self.init()

    def init(self):
        self.app = Flask(self.module.name)
        self.container.set('app', self.app)
        self.container.set('NestApplicationContext', self)
        self.container.set('NestContainer', self.container)
        self.container.set('NestLogger', self.logger)
        self.setupErrorHandlers()
        self.module.initControllers(self.container)

    def setupErrorHandlers(self):
        NestErrorHandler(self.app, self.logger)

    def getModule(self):
        return self.module

    def getOptions(self):
        return self.options

    def getContainer(self):
        return self.container

    def getLogger(self):
        return self.logger

    def listen(self, port=3000):
        self.logger.log('NestApplicationContext listen')
        return self.container.get('app')
