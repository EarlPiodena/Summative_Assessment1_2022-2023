marks = [("CodeLab I",67),
         ("web Development", 75),
         ("CodeLabII",74),
         ("Smartphone Apps",68),
         ("Games Development",70),
         ("Responsive web",65)]

print("Lowest to highest marks:")
marklh_sort = sorted(marks, key=lambda x : x[1])
print(marklh_sort)

print("Highest to lowest marks:")
markhl_sort = sorted(marks, key=lambda x: x[1], reverse=True)
print(markhl_sort)