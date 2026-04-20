def check_parentheses(expr):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0

expr = input("Enter expression: ")
print("Balanced" if check_parentheses(expr) else "Not Balanced")