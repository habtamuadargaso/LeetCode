class Two_sum() :
    def twosum(nums, target): 
        for i in range (len(nums)):
            for j in range(i+2,len(nums)):
                if nums[i] +nums[j] == target :
                    print("target with sum",target, "is:(", nums[i],",",nums[j],")")
    nums =[3,5,2,-4,8,11]         
    target = 7

    twosum (nums,target)         
                