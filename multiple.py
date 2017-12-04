#!При запуске команды из консоли, программа принимает на вход число,
# на выходе выдает значение True/False, в зависимости, кратно ли введенное число числу 3.


def mult (n):
        if n % 3 == 0:
            print(True)
        else: print(False)
try:
    number = int(input("Enter number: "))
    mult(number)
except ValueError:
    print("Input Error")
