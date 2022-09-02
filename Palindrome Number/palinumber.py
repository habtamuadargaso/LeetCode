import numbers
from operator import gt
import re


# First let define Class name 
class Palindrom_Num():
    # the funcation that recieve the number 
    def isPalinumber(num):
        number = num
        # palidrome number are always greater than from zero and postive numbers
        if num < 0 : 
            return False 
        # define the variable that holds the reverse palidrome number 
        reverse = 0 
        # while break when num = 0
        # The recursive function to reverse
        while (num >0  or num !=0 ):
            reverse = reverse * 10 + num % 10  
            num = num // 10 
        # then check the condition that number is palidrome or not 
        if (number == reverse):
        
            return True
        # then forward and backward the number is not equale then preturn false 
        else: 
           return False   
    # Driving code    
    num = int(input("Enter a number:"))
    print(isPalinumber(num))
    
    