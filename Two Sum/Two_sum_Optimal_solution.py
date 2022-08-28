def twoSumHashing(num_arr, pair_sum):
    sums = []
    # Initialize an empty hash table.
    hashTable = {}

    for i in range(len(num_arr)):
        # Calculate the complement by subtracting the current list element from the given number
        complement = pair_sum - num_arr[i]
        # Look up the complement in the hash table. If it exists, a pair that sums up to the given number has been found.
        if complement in hashTable:
            print("Pair with sum", pair_sum,"is: (", num_arr[i],",",complement,")")
        # Insert the current element of the array into the hash table after you perform the step above.    
        hashTable[num_arr[i]] = num_arr[i]

# Driver Code
num_arr = [4, 5, 1, 8]
pair_sum = 9    
  
# Calling function
twoSumHashing(num_arr, pair_sum)