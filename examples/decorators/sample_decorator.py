def simple_decorator(func):
    def wrapper(*args, **kwargs):
        return f'Decorated -- {func(*args, **kwargs)} -- Decorated'
    return wrapper


@simple_decorator
def hello():
    return 'Hello '


if __name__ == '__main__':
    print(hello.__name__)
    print(hello())
    print