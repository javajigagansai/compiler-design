grammar = {
    'E': ['E+T', 'T'],
    'T': ['T*F', 'F'],
    'F': ['(E)', 'id']
}

leading = {k: set() for k in grammar}
trailing = {k: set() for k in grammar}

for k in grammar:
    for prod in grammar[k]:
        leading[k].add(prod[0])
        trailing[k].add(prod[-1])

print("Leading:", leading)
print("Trailing:", trailing)