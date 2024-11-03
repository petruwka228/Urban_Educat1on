def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
try:
    inner_function()
except NameError as e:
    print(e) # NameError: name 'inner_function' is not defined