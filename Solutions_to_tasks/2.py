# Напишите функцию recursive_digit_sum, которая находит сумму всех цифр натурального числа.


def recursive_digit_sum(number):
    if number < 10:
        return number
    return (number % 10) + recursive_digit_sum(number // 10)


result = recursive_digit_sum(123)
print(result)
result = recursive_digit_sum(7321346)
print(result)