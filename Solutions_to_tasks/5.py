# write a decorator

def sum(f):

    def inner(*args, **kwargs):

        a = args[0]
        b = args[1]

        return f(*args, **kwargs), a - b
    
    return inner

@sum
def look_to_do(x, y):
    return x + y

print(look_to_do(10, 6))
print(look_to_do(10, -1))


def answer(f):

    def inner(*args, **kwargs):

        return f"Результат функции: {f(*args, **kwargs)}"
    
    return inner

@answer
def look_to(x, y):
    return x + y

print(look_to(10, 6))
print(look_to(10, -1))

