import matplotlib.pyplot as plt

table = plt.figure()
events = ['Game', 'Commercials', "Won't watch"]
male = [279, 81, 132]
female = [200, 156, 160]

tick_label = ['Game', 'Commercials', "Won't watch"]
color = ['#F6EA7BFF', '#FFBA52FF', '#E683A9FF']

plt.bar(events, male, color='blue')
plt.bar(events, female, bottom= male, color='red')

plt.xlabel('Poll Questions')
plt.ylabel('Number of Americans aged 18 and over')

plt.title('Answers to the poll')

plt.show()