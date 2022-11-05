age_years = input("What is your age in years?")
age_days = (int(age_years) * 365)
print(age_days)

## using f-string to display a more user-friendly result
print(f"You are {age_days} days old. You don't look a day over {age_days - 1}!")