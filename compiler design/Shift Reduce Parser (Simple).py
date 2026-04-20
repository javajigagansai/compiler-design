stack = []
input_str = list(input("Enter string (id+id): "))
grammar = {"E+E": "E", "id": "E"}

while True:
    if ''.join(stack) == 'E' and not input_str:
        print("Accepted")
        break
    
    if input_str:
        stack.append(input_str.pop(0))
    
    for key in grammar:
        if ''.join(stack).endswith(key):
            stack = list(''.join(stack).replace(key, grammar[key]))
            break
    else:
        if not input_str:
            print("Rejected")
            break