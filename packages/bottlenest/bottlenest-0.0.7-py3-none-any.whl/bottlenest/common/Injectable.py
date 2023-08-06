def Injectable():
    def wrapper(providerClass):
        return NestInjectable(
            providerClass=providerClass,
        )
    return wrapper


class NestInjectable:
    def __init__(self, providerClass):
        self.name = providerClass.__name__
        self.__name__ = providerClass.__name__
        self.providerClass = providerClass
        self.instance = None
        # self.dependencies = []

    def setup(self, module, container):
        # self.dependencies = []
        # for dep in self.dependencies:
        #     dep.setup(container)
        self.module = module
        self.container = container
        container.set(self.getProviderName(), self)
        self.instance = self.providerClass(container)

    def getProviderName(self):
        providerName = f"{self.module.name}.{self.name}"
        return providerName

    def __repr__(self):
        return f"{self.name}()"

    def __str__(self):
        return f"{self.name}()"
