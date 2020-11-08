inp_str = input("enter input in strings:")
print(inp_str)
"""lets initialize len to 0"""
str_length =0
"""using loop count the string indexes"""
for ch in inp_str:
    str_length = str_length + 1
print("Given input string is :{} s\n  The total string length is: {}".format(inp_str, str_length))