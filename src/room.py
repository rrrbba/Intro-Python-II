# Implement a class to hold room information. This should have name and
# description attributes.

#added none because getting typeerror that init is missing 4 required positional arguments
class Room():
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.n_to = None 
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = item
