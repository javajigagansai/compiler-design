word = input("Enter word: ")

v = sum(1 for ch in word if ch.lower() in 'aeiou')
c = sum(1 for ch in word if ch.isalpha() and ch.lower() not in 'aeiou')

print("Vowels:", v, "Consonants:", c)