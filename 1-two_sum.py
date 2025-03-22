from collections import defaultdict

def twoSum(nums, target):
    x = defaultdict(list)
    for i in range(len(nums)):
        if x[target-nums[i]] != []:
            return i, x[target-nums[i]][0]
        else:
            x[nums[i]].append(i) 


print(twoSum([1,2,3,4,5,7], 3))