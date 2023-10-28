# задача на использование стека при решении задач со скобками

def check(line):

    stack = []
    ex_sequence = '(){}[]'
    open_sequence = '([{'
    close_sequence = ')]}'
    first_commit_of_open = 0

    for index in range(len(line)):
        if line[index] in ex_sequence:

            if line[index] in open_sequence:
                if line[index] == "(":
                    stack.append(line[index])
                    if len(stack) == 0:
                        first_commit_of_open = index
                if line[index] == "[":
                    stack.append(line[index])
                    if len(stack) == 0:
                        first_commit_of_open = index
                if line[index] == "{":
                    stack.append(line[index])
                    if len(stack) == 0:
                        first_commit_of_open = index
                
                    
            if line[index] in close_sequence:
                if line[index] == ")":
                    if len(stack) != 0 and stack[-1] == '(':
                        stack.pop()
                    else:
                        return (index + 1)
                if line[index] == "]":
                    if len(stack) != 0 and stack[-1] == '[':
                        stack.pop()
                    else:
                        return (index + 1)
                if line[index] == "}":
                    if len(stack) != 0 and stack[-1] == '{':
                        stack.pop()
                    else:
                        return (index + 1)    
            

    if len(stack) == 0:
        return "Success"
    else:
        return (first_commit_of_open + 1)
    
data = input()
print(check(data))