code = [
    "t1 = b + c",
    "a = t1"
]

for line in code:
    if '+' in line:
        parts = line.split('=')
        temp = parts[0].strip()
        b, c = parts[1].split('+')
        print(f"ADD {b.strip()}, {c.strip()}")
        print(f"MOV {temp}, R")
    else:
        lhs, rhs = line.split('=')
        print(f"MOV {rhs.strip()}, {lhs.strip()}")