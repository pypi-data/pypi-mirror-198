from abc import ABC, abstractmethod, ABCMeta

# this context is given to the controller


class NestProviderContext(ABC):
    def __init__(self, cls):
        self.provider = cls

    def get(self, key):
        getName = f"{self.provider.module.name}.{key}"
        return self.provider.context.get(getName)

    def inject(self, injectable):
        key = injectable.__name__
        getName = f"{self.provider.module.name}.{key}"
        provider = self.provider.context.get(getName)
        if provider is None:
            raise Exception(f"Provider not found: {getName}")
        return provider.instance
