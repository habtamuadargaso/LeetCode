from audioop import reverse


class palindrome:
    # the recursive function to reverse
    def isPalindrome(num):
        # We can also read input as string and then simply check for palindrome.
        num = str(input("Enter here string or integer numbers: "))
        print ("The orignal number:", num)
        
        reverse = num[::-1]
        
        # for checking a number is palindrome
        if num == reverse :
            res = True
        else:
            res = False
        # printing result    
        print(res)    
        
var = palindrome()
var.isPalindrome()       