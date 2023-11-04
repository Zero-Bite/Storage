
line = list(filter(lambda x: x[0] not in 'Vv', [j for j in input().split('; ')]))
for element in line:
    if element[0] == "*":
        element = element.replace("*", '')
        print(element)
    else:
        print(element)
