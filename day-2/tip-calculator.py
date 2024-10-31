print("Welcome to the tip calculator!\n")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10,12, or 15? "))
num_people = int(input('How many people to split the bill? '))

tip_percent = tip / 100
bill_per_person = ((total_bill * tip_percent) + (total_bill)) / 7
print(f"Each person should pay: ${round(bill_per_person, 2)}")
