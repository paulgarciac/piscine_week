class Foo(object):
    def getbar(self):
        return self.bbar
    def setbar(self, value):
        if not isinstance(value, int):
            raise TypeError("bar must be set to an integer")
        self.bbar = value
    bar = property(getbar, setbar)

f = Foo()
f.bar = 3

print(f.bar)
