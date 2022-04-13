class Borg:
    
    """The Borg design pattern"""

    _shared_data = {} # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data # makes an attribute dictionary



class Singleton(Borg): # this will inherit from the borg class
                        # makes borg object an object oriented form of global variables    
    
    """The singleton class"""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs) # update the attribute dictionary by inserting a new key-value pair

    def __str__(self):
        return str(self._shared_data) # Returns the attribute dictionary for printing 

# Let's create a singleton object and add our first acronym
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
   
# Print the object
print(x)

# Let's create another singleton object and 
#if it refers to the same attribute dictionary
#by adding another acronym
y = Singleton(SNMP = "Simple Network Management Protocol")

# will retain previous acronym and add this one

# print the object
print(y)

