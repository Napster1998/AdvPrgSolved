# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Hell
# HellHell
# HellHellHell
# HellHellHellHell

mainInput = input().split()
wAmount,balInput = int(mainInput[0]),float(mainInput[1])

if balInput<wAmount:
    print(balInput)
elif wAmount%5 == 0:
    print(balInput-wAmount-0.50)

