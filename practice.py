currentAge = input("Enter your current Age: ")
lifeRemaining = 90 - int(currentAge)
days = lifeRemaining*365
months = lifeRemaining*12
weeks = lifeRemaining*52.16

print(f'Days: {int(days)}, Months: {int(months)}, Weeks: {int(weeks)}')