# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance

# base class
class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"

# base class
class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"

# subclass
class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)
        

c = C()
c.showprops()
print(C.__mro__)