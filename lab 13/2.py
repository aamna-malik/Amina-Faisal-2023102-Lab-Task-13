class HookedClassCreationMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")

        # Intercept attribute addition
        for attr_name, attr_value in dct.items():
            print(f"Adding attribute: {attr_name}")

        # Intercept method creation
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                print(f"Adding method: {attr_name}")

        # Create the class
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=HookedClassCreationMeta):
    class_variable = "I am a class variable"

    def __init__(self, value):
        self.instance_variable = value

    def method(self):
        print("This is a method")

# Output:
# Creating class MyClass
# Adding attribute: class_variable
# Adding attribute: __module__
# Adding attribute: __qualname__
# Adding attribute: __init__
# Adding method: __init__
# Adding attribute: method
# Adding method: method