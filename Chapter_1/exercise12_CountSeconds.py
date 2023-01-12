num_days = int(input("Enter number of days: "))

#coverting days into hours, hours to minutes, and minutes to seconds. 
#multiplies the day by 86400 seconds in a day
print(f"There are {(num_days * 24) * 60**2} seconds in {num_days} days.")