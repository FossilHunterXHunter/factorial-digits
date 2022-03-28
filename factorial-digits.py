import numpy
import sys
from fractions import Fraction as frac

#function that gets the sum of the factorial digits
def SumOfFractorial(n):
    FinalValue = 0

    #while loop to obtain each digit until n is less than 10
    while True:
        Remainder = numpy.remainder(n,10)   #gets the last digit from the number
        n = frac(numpy.floor_divide(n,10))  #divides the number by 10 towards minus infinity and uses Fraction library to keep precision
        FinalValue = numpy.add(FinalValue,Remainder)    #add single digit to the final value

        if(n<10):
            FinalValue = numpy.add(FinalValue,n)    #add last digit to final value
            print(FinalValue)   #print final sum
            break   #exit while loop

#try and except to see if there is an input or not
try:
    #use try and except to see if any letters are entered instead of digits
    try:
        #using eval function to evaluate the input as an expression and returns it as an integer
        digit = eval(sys.argv[1])
    except:
        print("Enter a number!")
        exit()  

    #check if it is a negative number
    if(digit<0):
        print("Enter a positive number!")
        exit()
#calculate the factorial using the numpy factorial function
    result = numpy.math.factorial(digit)
    
#get the sum of the digits in the factorial using SumOfFactorial function created 
    SumOfFractorial(result)

#print error if there is no input
except EOFError as e:
    print(e)