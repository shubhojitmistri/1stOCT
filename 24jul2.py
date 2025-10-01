# Prompt the user to input the number of rows
row_num = int(input("Input number of rows: "))

# Prompt the user to input the number of columns
col_num = int(input("Input number of columns: "))

# Create a 2D list (a list of lists) filled with zeros using list comprehension
# The outer list will have 'row_num' elements and the inner lists will have 'col_num' elements
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# Nested loop to populate the 2D list with multiplication results
for row in range(row_num):
    for col in range(col_num):
        # Set the value at position [row][col] in the 2D list to the product of 'row' and 'col'
        multi_list[row][col] = row * col

# Print the resulting 2D list containing the multiplication table
print(multi_list) 