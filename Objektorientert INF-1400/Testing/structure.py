class Foo():
    _struct = None
    def __new__(cls, *args, **kwargs):
        if not cls._struct:
            print ("Creating Instance")
            cls._struct = super(Foo, cls).__new__(cls)
        return cls._struct

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def bar(self):
        pass


i = Foo(100, 200)
print(i.a)
g = Foo(400, 500)
print(g.a)
print(i.a)