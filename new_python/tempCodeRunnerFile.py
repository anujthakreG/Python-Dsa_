s = len(nums)
# return new list 
result = [0] * s
p = 0 
n = 1
for i in range(s):
    if nums[i] >= 0 :
        result[p] = nums[i]
        p+=2
    else :
        result[n] = nums[i]
        n+=2
print(result)