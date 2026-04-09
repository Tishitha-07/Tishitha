class Joint:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y
