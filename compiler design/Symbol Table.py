symbol_table = {}

n = int(input("Enter number of variables: "))

for _ in range(n):
    name = input("Name: ")
    dtype = input("Type: ")
    symbol_table[name] = dtype

print("Symbol Table:")
for k, v in symbol_table.items():
    print(k, ":", v)