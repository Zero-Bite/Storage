# Напишите функцию make_equation, которая по заданным коэффициентам строит строку, 
# описывающую валидное с точки зрения Python выражение без использования оператора возведения в степень.

def make_equation(*args):
    if len(args) == 1:
        return f"{args[0]}"
    return f"({args[0]} * x + {args[1]}) + {make_equation(*args[2::])} * x"

result = make_equation(3, 2, 1)
print(result)