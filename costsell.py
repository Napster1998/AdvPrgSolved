
num1 = 123

reversed_num1 = 0

num2 = num1

while num2 != 0:                                    1                    12                                  123
    digit = num2 % 10                               1               2                             3
    reversed_num1 = reversed_num1 * 10 + digit      321               32                            3
    num2 //= 10                                     0                                  1                            12
print(reversed_num1, " ", num1)

