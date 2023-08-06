def Module(controllers=[], imports=[]):
    def wrapper(moduleClass):
        return NestModule(
            moduleClass=moduleClass,
            imports=imports,
            controllers=controllers,
        )
    return wrapper


class NestModule:
    def __init__(self, moduleClass, imports, controllers):
        self.name = moduleClass.__name__
        self.imports = imports
        self.controllers = controllers
        # self.moduleClass = moduleClass
        # self.moduleInstance = moduleClass()
        self.name = moduleClass.__name__
        print(f"NestModule init", [self.name])

    def initControllers(self, container):
        for imp in self.imports:
            imp.initControllers(container)
        for cont in self.controllers:
            cont.initController(container)
