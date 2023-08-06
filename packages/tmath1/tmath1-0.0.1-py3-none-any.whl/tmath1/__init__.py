import random
import os
import datetime

pi = 22 / 7
def developerName():
    print("Taus Hasan")
def add(*a):
    print(sum(a), "\n")
def multi(*args):
    z = 1
    for num in args:
        z *= num
    print("Answer is ", z, "\n")
def divr(a, b):
    x = a / b
    y = a % b
    print(f"Qoutient is {x} and remainder is {y}\n")
def div(a, b):
    x = a / b
    print(x)
def minus(a, b):
    print("Answer is ", a - b, "\n")
def pow(a, b):
    x = a ** b
    print("Answer is ", x, "\n")
def ran(a):
    x = random.choice(a)
    print(x)
def gennum(a, b):
    cb = random.randint(a, b)
    print(cb)
def mix(a):
    b = random.shuffle(a)
    print(b)
def weight(kg):
    x = kg * 9.81
    print(x, " Newton")
def weightinmoon(a):
    x = a * 9.81
    y = x / 6
    print(y, " Newton")
def positivity(num):
   if num > 0:
       print(f" {num} is a Positive number")
   elif num == 0:
       print(f"{num} is Zero")
   else:
       print(f" {num} is a Negative number")
def oddOrEven(num):
    if num/2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")    
def leapYear(year):
    if (year % 4) == 0:
        print(f"{year} is a leap year")
    elif (year % 100) == 0:
        print(f"{year} is a leap year")
    elif (year % 400) == 0:
       print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")    
def primeList(lower,upper):        
        
    print("Prime numbers between",lower,"and",upper,"are:")
    
    for num in range(lower,upper + 1):
       # prime numbers are greater than 1
    
       if num > 1:
           for i in range(2,num):
    
               if (num % i) == 0:
                   break
    
           else:
               print(num)     
def prime(num):
    if num > 1:
       # check for factors    
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               break    
       else:
           print(num,"is a prime number")
    
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(num,"is not a prime number")
def factorial(num,factorial):    
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")    
    elif num == 0:
       print("The factorial of 0 is 1")    
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
    
       print("The factorial of",num,"is",factorial)
def multiplicationTable(num,count,to):
    while count < (to+1):
        print(num, ' x ', count, ' = ', num * count)
        count = count + 1
def armstrongList(lower,upper):
    
    for num in range(lower, upper + 1):
    
       # order of number
       order = len(str(num))
    
       # initialize sum
       sum = 0
    
       # find the sum of the cube of each digit
       temp = num
    
       while temp > 0:
           digit = temp % 10
           sum += digit ** order
           temp //= 10
    
       if num == sum:
           print(num)
def convDecimel(dec):
    print(bin(dec))   
def convOctal(dec):
    print(oct(dec),) 
def convHexadecimel(dec):
    print(hex(dec))  
def asciiValue(a):
    print(ord(a))
def factor(a):
    lr = 1
    n = a
    ur = n

    for i in range(lr, ur + 1):
        if (n % i == 0):
            print(i)
def multiple(a):
    lr = 1
    n = a
    ur = n

    for i in range(lr, ur + 1):
        if (n % i == 0):
            print(i)
def getWord(a):
    with open(a, "r") as file:
        allText = file.read()

        words = list(map(str, allText.split()))
        x = random.choice(words)
        print(x)
def numLine(a,b):
    for i in range(a,b):
        print(i)


def commands():
    print("developerName()\nadd(numbers)\nmulti(numbers)\ndivr(a, b)\ndiv(a, b)\nminus(a, b)\npow(a, b)\nran(a)\ngennum(a, b)\nmix(a)\nweight(kg)\nweightinmoon(a)\npositivity(num)\noddOrEven(num)\nleapYear(year)\nprimeList(lower,upper)\nprime(number)\nfactorial(num,factorial)\nmultiplicationTable(num,count,to)\narmstrongList(lower,upper)\nconvDecimel(dec)\nconvOctal(dec)\nconvHexadecimel(dec)\nasciiValue(a)\nfactor(a)\nmultiple(a)\ngetWord(file name)\nnumLine(from,to)")

