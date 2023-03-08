#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator! \n")

bill = float(input("What was the total bill? \n$"))
tip = int(input("What percent of tip would you like to give 10, 12 or 15? \n"))
people = int(input("How many people are splitting the bill? \n"))

bill_with_tip = tip / 100 * bill + bill
per_person = float(bill_with_tip / people)
final_amount = round(per_person, 2)
print(f"Each person should pay ${final_amount}.")
