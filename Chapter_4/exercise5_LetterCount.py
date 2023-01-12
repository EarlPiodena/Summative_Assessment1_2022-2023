with open('sentences.txt') as file_handler:
    texts = file_handler.read()

occ_let = texts.split()

num_let = {}

for i in occ_let:
    for letter in i:
        if letter in num_let:
            num_let[letter] += 1
        else:
            num_let[letter] = 1

print("The number of occurrences of each letter in the file are:")

for key in num_let.keys():
    print(f"{key} : {num_let[key]}")