from ..metaClasses.NestProvider import NestProvider


def Injectable():
    def wrapper(originalClass):
        return NestInjectable(
            originalClass=originalClass,
        )
    return wrapper


class NestInjectable(NestProvider):
    __name__ = 'NestInjectable'

    def __init__(self, originalClass):
        # self.__name__ = originalClass.__name__
        self.cls = originalClass
        self.providerName = originalClass.__name__
        self.originalClass = originalClass
        self.classInstance = None
        # self.dependencies = []

    def getName(self):
        return self.providerName

    def eventName(self):
        return self.providerName

    # def enableProvider(self):
    #    pass

    def setupInjectable(self, module, container):
        print(
            f"NestInjectable setupInjectable {self.providerName} {container}")
        # self.module = module
        # self.container = container
        # TODO: This should be a singleton manager
        self.classInstance = self.originalClass(container)
        # providerName = f"{module.moduleName}.{self.providerName}"
        providerName = self.providerName
        container.set(providerName, self)

    def __repr__(self):
        return f"{self.providerName}()"

    def __str__(self):
        return f"{self.providerName}()"
