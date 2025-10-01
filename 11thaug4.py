# License: https://bit.ly/3oLErEI

# Define a function named 'test' that takes an integer 'n' as input
def test(n):
    # Check if 'n' is congruent to 4 modulo 34 and greater than 4^4
    return n % 34 == 4 and n > 4 ** 4

# Assign a specific integer 'n' to the variable
n = 922

# Print the original integer
print("Original Integer:")
print(n)

# Print the result of the test function applied to the integer 'n'
print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")
print(test(n))

# Assign a different integer 'n' to the variable
n = 914

# Print the original integer
print("\nOriginal Integer:")
print(n)

# Print the result of the test function applied to the modified integer 'n'
print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")
print(test(n))

# Assign another integer 'n' to the variable
n = 854

# Print the original integer
print("\nOriginal Integer:")
print(n)

# Print the result of the test function applied to the modified integer 'n'
print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")
print(test(n))

# Print the original integer again (note: the variable 'n' retains its previous value)
print("\nOriginal Integer:")
print(n)

# Print the result of the test function applied to the integer 'n' (no modification to 'n' since the previous assignment)
print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")
print(test(n))
