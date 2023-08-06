from bottlenest.core.NestModuleContext import NestModuleContext
from bottlenest.core.NestLogger import NestLogger
from bottlenest.transports.http.HttpTransport import HttpTransport


class NestApplicationContext:
    def __init__(self, module, transport):
        self.logger = self.__setupLogger()
        self.module = module
        self.module.enableModule()
        self.moduleName = module.moduleName
        self.moduleContext = self.__setupModuleContext(
            module=module,
            logger=self.logger,
        )
        # Calls NestHttpModule.setup()
        # self.setup()
        self.module.setupModule(
            appContext=self,
            moduleContext=self.moduleContext,
            transport=transport,
        )

    # def setup(self):
    #     # self.app = self.transport
    #     # self.moduleContext.set('transport', self.transport)
    #     # self.moduleContext.set('NestApplicationContext', self)
    #     # self.moduleContext.set('NestModuleContext', self.moduleContext)
    #     # Calls NestHttpModule.setup()
    #     self.module.setup(self.moduleContext)

    def __setupLogger(self):
        logger = NestLogger()
        return logger

    def __setupModuleContext(self, module, logger):
        moduleContext = NestModuleContext()
        moduleContext.set('module', module)
        moduleContext.set('logger', logger)
        return moduleContext

    def listen(self):
        self.logger.log('NestApplicationContext listen')
        self.module.listen()
