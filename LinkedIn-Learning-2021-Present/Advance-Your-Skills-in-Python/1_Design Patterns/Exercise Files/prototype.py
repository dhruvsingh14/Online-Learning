import copy

class Prototype:
    
    def __init__(self): # simply creating a dictionary object
        self._objects = {}
        
    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj # dictionary
        
    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name] # name is the key
        
    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name)) # most important method
        obj.__dict__.update(attr)
        return obj
        
class Car:
    def __init__(self):
        self.name = "Skylark" # initialize using defaults
        self.color = "Red"
        self.options = "Ex"
        
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)
        
c = Car()
prototype = Prototype() # prototype object out of prototype class
prototype.register_object('skylark', c)

# seeing if we can clone object
c1 = prototype.clone('skylark')

# printing the cloned object
print(c1)
