from ast import Num


# This function returns value of each Roman symbol
class Solution:
    def romanToInt(s: str):
        
        roman_table = {
            "I":  1,
            "V":  5,
            "X":  10,
            "L":  50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        last = "I"
        # Reverse iteration solution 
        for numeral in s[::-1]:
            # chek the numeral valeus in the roman table list 
            print((numeral,  roman_table[numeral]))
            # for example when the roman number  fours is IV (I = 1 and V = 5) . 
            # This case check the condition left to right is smaller always otherwise make first number-last (V-I) to get 4 
            if roman_table[numeral] < roman_table[last]:
                
                total  -= roman_table[numeral]
            else :
                total += roman_table[numeral]    
                last = numeral
          
        return total    
    print(romanToInt("XL"))