count = 0

with open('sentences.txt') as file_handler:
    for lines in file_handler.readlines():
        if lines.strip() == 'Hello my name is Amster Sani':
            count += 1
        else:
            continue

print("The number of times the sentence 'Hello my name is Amster Sani' occured is", count)