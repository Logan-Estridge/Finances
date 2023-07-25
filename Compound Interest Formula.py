# Formula for computing final amount (A) on compounding interest after some time.
# A = P*((1+(r/n))**(n*t))
# Where: P is the principal amount (initial investment), r is the nominal interest rate (as a decimal),
# n is the number of times the interest is compounded per unit time, and t is the chosen increment of time.

P = int(input("Principal amount: "))
r = float(input("annual nominal interest rate (as a decimal): "))
n = int(input("number of times the interest is compounded per chosen time increment: "))
t = int(input("number of time increments: "))

A = P*((1+(r/n))**(n*t))
print(A.__round__(2))



