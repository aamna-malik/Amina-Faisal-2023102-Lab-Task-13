class AttributeValidationMeta(type):
    def __new__(cls, name, bases, dct):
        # Custom attribute validation
        for attr_name, attr_value in dct.items():
            if attr_name.endswith('_validated') and not isinstance(attr_value, int):
                raise TypeError(f"{attr_name} must be an integer")

        # Create the class
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=AttributeValidationMeta):
    validated_attribute = 42
    non_validated_attribute = "string"

    def __init__(self):
        pass

# This will raise a TypeError because 'non_validated_attribute' is not an integer
# MyClass()