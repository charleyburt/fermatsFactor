# Charley Burtwistle
# March 7, 2018

import math
from sympy import pretty_print as pp

#-----------------------------------------------------

def getValue():
    n = int(input("Enter odd integer you would like to factor. Press ENTER when finished: "))
    guess = math.ceil(math.sqrt(int(n)))
    fermatsFactor(n, guess)


def fermatsFactor(n,guess):
    perfect = (int(guess)**2) - int(n)
    sqrt_perfect = math.sqrt(perfect)

    while not sqrt_perfect.is_integer():
        print('%d^2 - %d = %d' %(guess,n,perfect))
        guess = guess + 1
        perfect = (int(guess)**2) - int(n)
        sqrt_perfect = math.sqrt(perfect)

    print('%d^2 - %d = %d' %(guess,n,perfect))
    print('\n %d = %d^2 - %d^2' %(n,guess,sqrt_perfect))
    print('\n %d = (%d+%d)(%d-%d)'%(n,guess,sqrt_perfect,guess,sqrt_perfect))



#-----------------------------------------------------
def getAll():
    n = 1
    while n < 1000000:
        guess = math.ceil(math.sqrt(int(n)))
        showThemAll(n,guess)
        n = n + 2

def showThemAll(n=1,guess=1):
    perfect = (int(guess)**2) - int(n)
    sqrt_perfect = math.sqrt(perfect)

    while not sqrt_perfect.is_integer():
        guess = guess + 1
        perfect = (int(guess)**2) - int(n)
        sqrt_perfect = math.sqrt(perfect)

    print('%d = (%d+%d)(%d-%d)'%(n,guess,sqrt_perfect,guess,sqrt_perfect))


if __name__ == "__main__":
    choice = int(input("\nEnter 0 to see how to factor a specific number.\nEnter 1 to see first 500,000 odd numbers factored.\nPress ENTER when finished: "))
    if choice == 0:
        getValue()
    elif choice == 1:
        getAll()
