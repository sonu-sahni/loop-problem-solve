# Find non repeted str
input_str = "teeterracacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print('Char is ', char)
        break