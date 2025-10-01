import decimal
import fractions

# Ask user to enter numbers separated by spaces
user_input = input("Enter decimal numbers separated by spaces: ")

# Convert each input to Decimal
values = [decimal.Decimal(num) for num in user_input.split()]

# Display fractions
for d in values:
    print(f"{d} = {fractions.Fraction(d)}")
