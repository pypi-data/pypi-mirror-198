from bottlenest.core.NestApplicationContext import NestApplicationContext


class NestFactory:
    @staticmethod
    def createMicroservice(module, options={}):
        instance = NestFactory.createApplicationContext(module, options)
        # load routes
        # instance.init()
        return instance

    @staticmethod
    def createApplicationContext(module, options={}):
        return NestApplicationContext(module, options)
