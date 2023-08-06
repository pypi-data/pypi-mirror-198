class NestModuleContext:
    def __init__(self):
        self.container = {}

    def set(self, key, value):
        print("NestModuleContext set", key, value)
        self.container[key] = value

    def get(self, key):
        print("NestModuleContext get", key)
        return self.container[key] if key in self.container else None

    # def inject(self, injectable):
    #     moduleName = self.container['module'].name
    #     providerName = injectable.__name__
    #     key = f"{moduleName}.{providerName}"
    #     provider = self.container[key] if key in self.container else None
    #     if provider:
    #         return provider.instance
    #     else:
    #         raise Exception(f"Provider not found: {key}")
