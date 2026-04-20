s = input("Enter string: ")

letters = digits = spaces = special = 0
for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special:", special)