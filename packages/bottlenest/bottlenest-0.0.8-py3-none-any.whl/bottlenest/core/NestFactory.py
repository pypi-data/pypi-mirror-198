from bottlenest.core.NestApplicationContext import NestApplicationContext
import os


class NestFactory:
    @staticmethod
    def createMicroservice(module, transport=None):
        instance = NestFactory.createApplicationContext(
            module=module,
            transport=transport,
        )
        # load routes
        # instance.setup()
        return instance

    @staticmethod
    def createApplicationContext(module, transport):
        return NestApplicationContext(
            module=module,
            transport=transport,
        )
