# Initialize variables 'x' and 'y' with values 0 and 1, respectively
x, y = 0, 1

# Execute the while loop until the value of 'y' becomes greater than or equal to 50
while y < 50:
    # Print the current value of 'y'
    print(y)
    
    # Update the values of 'x' and 'y' using simultaneous assignment,
    # where 'x' becomes the previous value of 'y' and 'y' becomes the sum of 'x' and the previous value of 'y'
    x, y = y, x + y