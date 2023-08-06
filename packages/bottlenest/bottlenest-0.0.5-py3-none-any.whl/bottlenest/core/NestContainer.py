class NestContainer:
    def __init__(self):
        self.container = {}

    def set(self, key, value):
        print("NestContainer set", key)
        self.container[key] = value

    def get(self, key):
        return self.container[key] if key in self.container else None
