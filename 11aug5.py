

# Define a function to check the condition
def test(n):
    return n % 34 == 4 and n > 4 ** 4

# Ask the user how many numbers they want to check
count = int(input("How many numbers do you want to check? "))

# Loop for each input
for i in range(count):
    n = int(input(f"Enter integer #{i+1}: "))
    print(f"Original Integer: {n}")
    print("Check whether the integer is greater than 4^4 and has a remainder of 4 when divided by 34:")
    print(test(n))
