# Пространство имен.


def test_function():
    def inner_function():
        return print("Я в области видимости функции test_function")

    inner_function()


# inner_function внутри функции test_function
test_function()

#  inner_function вне функции test_function
inner_function()