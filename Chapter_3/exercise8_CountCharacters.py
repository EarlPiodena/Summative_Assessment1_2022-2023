let = input("Enter word(s): ")

vcount = 0
ccount = 0
scount = 0
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

for x in let.lower():
    if x in vowels:
        vcount += 1
    elif x in consonants:
        ccount += 1
    else:
        scount += 1

print(f"Length of the word/given sentence: {len(let)}\nThe amount of vowels: {vcount}\nThe amount of consonants: {ccount}\nThe amount of special characters: {scount}")