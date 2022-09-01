class Two_sum() :
    # define the funcation 
    def twosum(nums, target):
        # search first list element in the array 
        for i in range (len(nums)):
             # search start from the second element from the  list element in the array 
            for j in range(i+1,len(nums)):
                # if the sum of two number is equal to target then print those numbers 
                if nums[i] +nums[j] == target :
                    print("target with sum",target, "is:(", nums[i],",",nums[j],")")
    # Drive Code 
    nums =[3,5,2,-4,8,11]         
    target = 7

    # funcation call inside the printe
    twosum (nums,target)         
                