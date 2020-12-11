from decimal import Decimal, getcontext
import math

prec = int(input("Enter how many digits of e you want to be returned: "))
getcontext().prec = prec + 1
e = Decimal(1)

iteration = int(input("Enter how many times do you want e's formula to be iterated: "))

for n in range(1, iteration + 1):
  e += Decimal((1 / math.factorial(n)))

e_txt = open(r"digits_of_e.txt", "a")
digitsofe = str(e)
e_txt.write(digitsofe)
e_txt.close()
