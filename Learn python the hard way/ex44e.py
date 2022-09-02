class Other(object):
    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")


class Child(object):

    def __init__(self):
        self.other = Other()

    def override(self):
        print("CHILD override()")
    
    def implicit(self):
        self.other.implicit()
    
    def altered(self):
        print("CHILD, BEFORE other altered()")
        self.other.altered()
        print("CHILD, AFTER other altered()")


son = Child()

son.override()
son.implicit()
son.altered()