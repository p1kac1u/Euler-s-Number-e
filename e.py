# run it on repl.it: repl.it/@p1kac1u/Eulers-Number-e#main.py

from decimal import Decimal, getcontext
import math

prec = int(input("Enter how many digits of e you want to be returned: "))
getcontext().prec = prec + 1
e = Decimal(1)
error = Decimal(0)

iteration = int(input("Enter how many times do you want e's formula to be iterated: "))

for n in range(1, iteration + 1):
  e += Decimal((1 / math.factorial(n)))
  error = Decimal((abs(Decimal(math.e) - Decimal(e))/Decimal(math.pi)*100)
  print(n, "|", e, "|", error, "%" )
