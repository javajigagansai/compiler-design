expr = input("Enter expression (a=b+c): ")

lhs, rhs = expr.split('=')
op = '+' if '+' in rhs else '-'
a, b = rhs.split(op)

print("Quadruple:")
print((op, a, b, 't1'))
print(('=', 't1', '-', lhs))

print("Triple:")
print((op, a, b))
print(('=', 0, '-', lhs))