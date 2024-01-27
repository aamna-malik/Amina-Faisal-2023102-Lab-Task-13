# Logging Mixin
class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {type(self).__name__}: {message}")

# Serialization Mixin
class SerializationMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

    def from_json(self, json_string):
        import json
        data = json.loads(json_string)
        self.__dict__.update(data)

# Example class using mixins
class MyClass(LoggingMixin, SerializationMixin):
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Using the class with mixins
obj = MyClass(name="example", value=42)

# Using logging method from LoggingMixin
obj.log("This is a log message")

# Using serialization methods from SerializationMixin
json_string = obj.to_json()
print(f"Serialized JSON: {json_string}")

# Creating a new instance and deserializing from JSON
new_obj = MyClass(name="", value=0)
new_obj.from_json(json_string)

# Verifying the deserialized object
print(f"Deserialized Object: {new_obj.__dict__}")
