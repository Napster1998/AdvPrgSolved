
num1 = 123

reversed_num1 = 0

num2 = num1

while num2 != 0:
    digit = num2 % 10
    print(digit)
    reversed_num1 = reversed_num1 * 10 + digit
    num2//= 10
print(reversed_num1," ", num1)

