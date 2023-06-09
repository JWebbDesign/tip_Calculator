# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

bill = input("Enter bill amount: ")
bill_as_float = float(bill)
tip = input("How much would you like to tip? 10, 12 or 15? ")
tip_as_int = int(tip)
guests_in_party = int(input("Enter the number of guests in the party: "))

tip_as_percent = tip_as_int / 100
tip_amount = bill_as_float * tip_as_percent
total_bill = bill_as_float + tip_amount
total_per_person = total_bill / guests_in_party
final_amount = round(total_per_person, 2)
final_amount = "{:.2f}".format(total_per_person)

print(f"Each guest in the party should pay ${final_amount}")
