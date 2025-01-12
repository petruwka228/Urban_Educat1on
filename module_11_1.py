import inspect

class MyObject:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привет, мое имя {self.name} и мне {self.age} лет.")

def introspection_info(obj):
    info = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not attr.startswith('__')],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else 'None',
    }

    if isinstance(obj, MyObject):
        info['other_properties'] = {
            'name': obj.name,
            'age': obj.age,
        }

    return info

number_info = introspection_info(42)
print(number_info)

my_object = MyObject('Диего', 30)
print(introspection_info(my_object))