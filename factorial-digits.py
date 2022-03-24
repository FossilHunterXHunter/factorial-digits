import numpy
import sys

#function that gets the sum of the factorial digits
def SumOfFractorial(n):
    FinalValue = 0
    while(n>10):
        ModValue = n %10
        n = n//10
        FinalValue = FinalValue + ModValue
    if(n<10):
        FinalValue = FinalValue + n
    print(FinalValue)

#try and except to see if there is an input or not
try:
    #use try and except to see if any letters are entered instead of digits
    try:
        #using eval function to evaluate the input as an expression and returns it as an integer
        digit = eval(sys.argv[1])
    except:
        print("Enter a number!")
        exit()  

#calculate the factorial using the numpy factorial function
    result = numpy.math.factorial(digit)

#get the sum of the digits in the factorial using SumOfFactorial function created 
    SumOfFractorial(result)

#print error if there is no input
except EOFError as e:
    print(e)