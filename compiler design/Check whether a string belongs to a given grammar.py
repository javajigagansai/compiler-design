def check_string(s):
    if s == "ab":
        return True
    if len(s) > 2 and s[0] == 'a' and s[-1] == 'b':
        return check_string(s[1:-1])
    return False

string = input("Enter string: ")
print("Valid" if check_string(string) else "Invalid")