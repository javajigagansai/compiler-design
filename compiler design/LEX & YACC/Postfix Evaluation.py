def eval_postfix(expr):
    stack = []
    for ch in expr:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == '+': stack.append(a+b)
            elif ch == '-': stack.append(a-b)
            elif ch == '*': stack.append(a*b)
            elif ch == '/': stack.append(a//b)
    return stack[0]

expr = input("Enter postfix: ")
print("Result:", eval_postfix(expr))