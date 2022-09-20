# ### `Exercise 1` override

# 1. Create a class that has at least one method
# 2. Create a subclass that uses your class (1) as base class
# 3. In the subclass(2) you should override the method from (1)
# 4. Print a instance of(1) and (2) both calling the same method name

class Guitars:
    def __init__(self, model):
        self.model = model

    def les_paul(self):
        print(self)
        print("That is a Fender!")


class Gibson(Guitars):
    def les_paul(self):
        print(self)
        print("Les pauls are Gibson only!")
