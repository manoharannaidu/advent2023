# print([line for line in open("./puzz1_test_input.txt")])
# lines = [line for line in open("./puzz1_test_input.txt")]
#
# print([
#     int(char) 
#      for line in open("./puzz1_test_input.txt") 
#      for char in line
#      if char.isdigit()
# ])
#

sum = 0
for line in open("./inputs/puzzel1_input.txt"):
    line_digits = [
        int(char) 
         for char in line
         if char.isdigit()
    ]

    sum = sum + (line_digits[0]*10) + line_digits[-1]

print(sum)
