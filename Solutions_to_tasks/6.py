
def result_accumulator(f):

    storage = []

    def inner(*args, method="accumulate"):
        
        nonlocal storage

        if method == 'drop':
            storage += [f(*args)]
            line = storage
            storage = []
            return line
        else:
            storage += [f(*args)]
            return None
        
    return inner

@result_accumulator
def a_plus_b(a, b):
    return a + b

print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))