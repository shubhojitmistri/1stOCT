result_str = ""
for row in range(0, 7):
    for coloumn in range(0, 7):
        if ((row in [0, 3, 6] and (coloumn > 1 and coloumn < 5)) or
            (coloumn == 1 and row in [1, 2, 6]) or
            (coloumn == 5 and row in [0, 4, 5])):
            result_str += "o"
        else:
            result_str += " "
    result_str += "\n"

print(result_str)

# Second part
row = 15
col = 18
result_str = ""

for i in range(1, row + 1):
    if (i <= 3) or (7 <= i <= 9) or (13 <= i <= 15):
        for j in range(1, col):
            result_str += "o"
        result_str += "\n"
    elif 4 <= i <= 6:
        for j in range(1, 5):
            result_str += "o"
        result_str += "\n"
    else:
        for j in range(1, 14):
            result_str += " "
        for j in range(1, 5):
            result_str += "o"
        result_str += "\n"

print(result_str)
