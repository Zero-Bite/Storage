# декоратор счетчика вызовов функции

def count(f):
    counter = 0

    # расширение исходной функции
    def decorator(*args, **kwargs):
        nonlocal counter
        counter += 1

        return f(*args, **kwargs), counter
       


    return decorator

@count
def what_number(name: str):
    return f"Hello, {name}"

print(what_number("Name"))
print(what_number("Look"))
print(what_number("Check"))
print(what_number("TOOL"))
