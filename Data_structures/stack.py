# задача на использование стека при решении задач со скобками

line = " "

stack = []
ex_sequence = '()'
open_sequence = '('
close_sequence = ')'
first_commit_of_open = 0

for index in range(len(line)):
    if line[index] in ex_sequence:
        if line[index] in open_sequence:

            if line[index] == "(":
                stack.append(line[index])
                if len(stack) == 0:
                    first_commit_of_open = index
                
        if line[index] in close_sequence:
            if line[index] == ")":
                if stack[-1] == '(':
                    stack.pop()
                else:
                    print(index)

if len(stack) == 0:
    print("Success")
else:
    print(first_commit_of_open)