# definiton for single-linke list
# this line defines a class named 'Listnode' 
class ListNode(object):
    # This is the constructor method for the ListNode class. It initializes the attributes of an instance of this class
    def  __init__(self, val = 0 , next= None):
        self.val = val
        self.next = next 
        
class Solution(object)  :
    def addTwoNumber(self, l1, l2):
        carry = 0 
        dummy_head = ListNode()
        current = dummy_head
        
        while l1 or l2 :
            x = l1.val if l1 else 0 
            y = l2.val if l2 else 0 
            total = x + y+ carry
            carry = total // 10
            current = current.next
            
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
        if carry > 0 :
            current.next = ListNode(carry)
       
        return dummy_head.next   
# Create linke list for the number 
                           
l1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents 243 (2 -> 4 -> 3)
l2 = ListNode(5, ListNode(6, ListNode(4)))  # Represents 465 (5 -> 6 -> 4)

# create an instance of the listnode 
 
solution = Solution ()

# call the addtwonumbers method to add the numbers

result = solution.addTwoNumber(l1, l2)


# print th reslut
while result:
    print(result.val, end= "")
    result = result.next()        