# starting again with the scratch
"""
Lecture 2 :
Time complexity :- Time taken to run the code (wrong definition) 
Rate of increase in time wrt input size 

The 3 rules to calculate time complexity :- 
1> Always calculate tc in terms of worst case 
2> avoid the constant values
3> avoid lower bound 

Types of time complexity :- 
1> Big-Oh (O) :- worst case (upper bound)
2> theta :- average case (worst + best / 2)
3> omega :- best case (lower bound)

Space cpmplexity :- memory taken -> big-O notation 
Auxilary space :- the extra space used to solve the problem 
+ input space :- space used to store the input 
"""

"""
Lecture 3:- 
What is tle (time limit exceeded error) -> when your operations gets eceeded than the time limit given 
basically sevrer can perform 10^8 operations in 1 second 
try to match the time complexity by the constraint given in the question --> just modify the code to reduce the tle 

lecture 4 :- time complexity realted to the operations learn from the ss taken 
"""



#----------------------------------------------------------------------------------------

"""
Lecture 5 - extraction of digits using loop :- count digits, reverse a number, check palindrome, armstrong number 

-> % 10 always gives the llast number and (//) floor division always gives the numbner without decimal like 5873 // 10 -> 587
always remember dont change the input given by the interviewer  
"""
n = 5873
nums = n
while nums > 0 :
    last_digit = nums % 10
    print(last_digit)
    nums = nums // 10


#----------------------------------------------------------------------------------------

"""
Lecture 6 
"""
# counting the number of digits , other way is to take the log vakue of the number and simply add 1 to it 
# log(5438) = 3.735 + 1 it is 4. something and total digits are 4  ---> simply do from math import *
print("counting number of digits")
n = 12345678
nums = n 
count = 0 
while nums > 0 :
    # print(last_digit)
    nums = nums // 10
    count = count + 1
print(count)      # base  = 10 , n = the nums 

# While calculating the TC always look the kind of operations it is happening inside the while loop 
# So--> whenever your iteration is number based -> TC == O(log,base = inside number (n)) , as the operation is happening in the two var only so the sc is O(1)


#----------------------------------------------------------------------------------------

"""
Lecture 7
"""

# reverse a number 
print("Reversing a number")

"""n = 123456
nums = str(n)

if nums == nums[::-1]: # this method is known as string slicing ,  .reverse() is only used in lists 
    print("True")
else:
    print("False")    # not used in interview"""

n = 1234
nums = n 
result = 0
while nums > 0 :
    ld = nums % 10 
    result = (result * 10) + ld
    nums = nums // 10
    # return n == result
print(result)
print(n == result)  # it will show you the boolean value , same TC as above 

#----------------------------------------------------------------------------------------

"""
lecture 8
"""

"""n = 153
nums = n 
sum = 0    
for i in range(nums):  -> loop is going upto 152 from 0 
    sum = sum + nums[i] ** 3  -> int can't be indexed , only list and strings can be 
 
print(sum == n)"""

print("armstrong number :- ")
n = 153 
nod = len(str(n))
total = 0
num = n 
while num > 0 :
    ld = num % 10
    total = total + (ld**nod)
    num = num // 10

print(total == n)

#----------------------------------------------------------------------------------------
"""
Lecture :- 9 :- Printt all the factors of the given numbers 
"""
# 1> Brute force -> has a high time complexity 
n = 20
num = n
result = []    
for i in range(1,num+1):
    if num % i == 0:
        result.append(i)
print(result)

# 2> better way -> tc :- o(n/2) almost similar to o(n)
n = 10
nums = n 
result = []
for i in range(1, (nums // 2) + 1):  # +1 to include the last element 
    if nums % i == 0:
        result.append(i)
result.append(nums)
print(result)

# 3> optimal solution :- loop goes to sqrt of the given number and store 2 var at a time
from math import sqrt
n = 36
nums = n 
result  = []
for i in range(1, int(sqrt(nums)) + 1):  # -> o(rootn)
    if nums % i == 0:
        result.append(i)
        if nums // i != i :
            result.append(nums // i ) 
result.sort()                           # -> on(nlogn)
print(result)

"""
Lecture : 10
"""

nums = [5,6,7,7,1,9,111,1,1,5,1,1]
freq_map = {}
for i in range(0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else :
        freq_map[nums[i]] = 1
print(freq_map)        # TC :- o(n) 

# 2nd method :- hash map    # the better method is freq map 
nums = [5,6,7,7,1,9,111,1,1,5,1,1]
n = len(nums)
hash_map = {}
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0) + 1  # if the value exists it will return that value if not then it will return 0 
print(hash_map)   # has better time complexity


"""
Lecture :- 11
"""
# Some of the hashing techniques :- store the daata in efficient way so searching is quite easy , and it is a kind of dict

# brute force way 
# give n and m can have 10^8 elements since the loop will operate the o(n *m) times the code will not be acccepted due to tle 
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
# for num in m :
#     count = 0
#     # print(num)
#     for x in m :
#         if x == num:
#             count+=1
#     print(count)

# optimal solution :-
hash_list  = [0] * 11
for num in n :             # tc is n 
    hash_list[num] += 1
for num in m:              # tc is m 
    if num < 1 or num > 10:
        print(0)
    else :
        print(num,":- ",hash_list[num])  # here the tc is o(n + m )


# third way is dict
n = [5,3,2,2,1,5,5,7,5,10]
dict = {}
for i in range(0, len(n)):
    if n[i] in dict:
        dict[n[i]] += 1
    else :
        dict[n[i]] = 1
print(dict)
for num in m :
    if num in dict:
        print(num, dict[num])
    else :
        print(num,0)  # this shows the clearness what is absent and what is present 


# Character hashing 


"""
Lecture :- 12 Intro to recussrion 

#  INfinite recurrsion :- it is not supported in c++,java , but python calls 987 recurrsion after that it shows the error
#  that is why we run the recurrsion until the base case is met  :- two types are there head and tail """ 


"""
Lecture :- 13 recurssion using parameters 
"""
# whenever the base case is met always do the returning to the start of the case 
# in the tail recu n to 1 :- print usually works after returning back 


# head print 1 to n :- pehle print hoga fir function call hoga
# tail recurrsion :- pehle function call hoga then the print work starts after the return calls

# example :- 1 to N :- head
print("head 1 to n :- ")
i = 1
n = 4
def func(i,n):
    if i > n :
        return
    print(i)
    func(i+1,n)

func(1,4)

print("head n to 1 :- ")
def hfunc(i,n):
    if n == 0:
        return
    print(n)
    hfunc(i,n-1)
hfunc(1,4)


print("tail n to 1 :- ")
def tfunc(i,n):
    if i > n :
        return
    tfunc(i+1,n)
    print(i)
tfunc(1,4)


print("tail 1 to n :- ")
def ttfunc(i,n):
    if n == 0:
        return
    ttfunc(i,n-1)
    print(n)

ttfunc(1,4)

"""
basically there are two types of recursion :- parameterized , funtional 
Lecture 14 :- what is functional recusrion 
"""
# what is parametrized function :- 
def nsum(sum,i,n):
    if i > n :
        print(sum)
        return    # but in this type of return it goes to the function which called him and it directly prints the total and the return is to stop the recusrion
    nsum(sum+i,i+1,n)

nsum(0,1,10)

# but when you dont print but reutrn something that is called as functional recusrsion
print("functional recursion :- ")
n = 10 
def ffcun(n):
    if n == 1:
        return 1 # means that function will return 1 not the whole answer will be one , kuch likh ke return kro to it is called as functional recursion
    return n + ffcun(n-1)   # you directly return here only 
x = ffcun(10)   # all the khichdi uppr se niche and then niche se uppr we will store and then print it 
print(x)    

# PENDING :- dry run if the above two recursion 
"""
lecture 15 :- print the factorial of the number 
"""

def fac(n):
    if n == 0:
        return 1

    return n * fac(n-1)
y = fac(4)
print(y)


"""
lecture 16 :- reversing an array using recursion 
"""
# using the method of recusrion :- 

nums = [1,2,3,4,5,6,7,8,9]

def revarray(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    revarray(nums, left+1, right-1)

def doit(nums, l, r):
    revarray(nums, l, r)

r = len(nums) - 1   # last index
doit(nums, 0, r)
print(nums)


"""
Lecture 17 :- check if a string is palindrome or not
"""

s = "hello"
print(s)

# iterative approach
n = len(s)
right = n - 1 
left = 0
def sfirst(s,left,right):
    while left < right :
        if s[left] != s[right]:
            return False
        left += 1
        right -=1

    return True
sfirst(s,left,right)
print(sfirst(s,left,right))
# print(s)

# recursion based appproach :-        ---> very good method 
print("recursion based approach")     # -> same as that of reversing a string
ss = "ABCABC"
left = 0 
n = len(ss)
right = n - 1
def function(s,left,right):
    if left >= right :
        return True
    if s[left] != s[right]:
        return False
    return function(s,left+1,right-1)

function(ss,0,n-1)


"""
Lecture 18 :- find the fibonacci number :- it is the sum of previous two number  
"""
print("\nfibo naci \n")
def fib(n):
    if n == 0 or n == 1 :
        return n  # it will return the value upward 
    return fib(n-1) + fib(n-2)

n = 5 
print(fib(n))

"""
Lecture 19 :- selection sort 
# TC :- as the loop works a total of n(n+1)/ 2 therefore :- o(n^2)
"""
nums = [9,8,7,6,5,4,3,2,1]
print(nums)

def selection(nums):
    n = len(nums)
    for i in range(0,n):
        min_ind = i
        for j in range(i+1,n):
            if nums[j] < nums[min_ind]:
                min_ind = j 
        nums[i], nums[min_ind] = nums[min_ind], nums[i]

print("after selection sort :- ")
selection(nums)
print(nums)


"""
Lecture 20 :- bubble sort :- by my own
"""
print("bubble sort :- ")
# the condition of outer and inner loop 
nums = [8,5,4,7,9,3,2,1,4,7,8,2,1]
print(nums)
def bubble(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):  # because the last poition will be get fixed by the element due to the outer loop
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
bubble(nums)
print(nums)

"""
Lecture 21 :- insertion sort 
tc :- same as selection sort 
"""
print("insertion sort :- ")
nums = [9,8,7,6,5,4,3,2,1]
print(nums)
def insertion(nums):
    n = len(nums)
    for i in range(0,n):
        key = nums[i]
        j = i - 1 
        while j >= 0 and nums[j] > key :
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
insertion(nums)
print(nums)


"""
tricky 
lecture 22 :- merge sort , works on the principle of divide and conquoer 
the logic for merge function is the number which you are appending in the final list after comparing increment that side
left_arr = nums[:mid]   # mid index is excluded
right_arr = nums[mid:]  # mid index is included

Time complexity and space complexity :- 
tc :- O(n logn )
sc :- O(n) because you store the elements in the result whenever you call the maerge_array function 
"""
print("merge sort :- ")
def merge_array(left, right):
    result = []
    i,j = 0,0
    n,m = len(left), len(right)
    while i < n and j < m :
        if left[i]<= right[j]:
            result.append(left[i])
            i+=1
        else :
            result.append(right[j])
            j+=1
    if i < n :  # this is the condition after the main loops finishes not inside the main loop otherwise the elements will be double copies/appended
        while i < n :
            result.append(left[i])
            i+=1
    if j < m :
        while j < m :
            result.append(right[j])
            j +=1
    return result 

def merge_sort(arr):
    if len(arr) <= 1 :
        return arr
    mid = len(arr) // 2 
    left_arr = arr[:mid]  # it means the mid th element is excluded  [::mid] -> this is different it includes the start stop step part 
    right_arr = arr[mid:]  # in this step is not written so python uses 1 as a default value 
    left = merge_sort(left_arr)  # we are just storing it in the variable so that we can pass it to other function 
    right = merge_sort(right_arr)
    return merge_array(left,right)

nums = [8,9,5,4,6,7,4,5,1,2,3]
print(nums)
print(merge_sort(nums))

# dry run the first iteration 

"""
lecture 23 :- quick sort , imp for interview 
questions :- best , worst , average case tc and the reason also 

remember merge sort gave us new array but we are fixing the position of the pivot element inside the array only , this is the benefit we are getting
i ka aisa element dhundo jo pivot se badha ho -> bada milte hi stop 
j ka aisa element dhundho jo pivot se kam ho 


TC :- O(log n * n ) :- for the best and average case 
worst case :- 
"""
print("quick sort")
nums = [4,1,7,6,3,2,8]
print(nums)
low = 0
high = len(nums) - 1 
# print(high)
def partition(nums,low,high):
    pivot = nums[low]
    i,j = low,high
    while i < j :
        while nums[i] <= pivot and i <= high - 1 :
            i+=1
        while nums[j] >= pivot and j >= low + 1 :
            j-=1
        if i < j :
            nums[i],nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j] , nums[low]  # because at the time of the process you will see j ke aage ke element lowth element se badhe hai 
    return j 

def quick_sort(nums,low,high):
    if low<high :
        p_index = partition(nums,low,high)
        quick_sort(nums,low,p_index - 1)
        quick_sort(nums,p_index + 1,high)

quick_sort(nums,low,high)
print(nums)



"""
Lecture 24 :- find the largest element in the array
tc :- O(n)
"""

print("find the largest element in the array")
nums = [55,32,-97,99,3,67]
largest = nums[0]
n = len(nums)
for i in range(n):
    largest = max(largest, nums[i])
print(largest)


"""
Lecture 25 :- find the second largest element in the array
"""

print("find the second largest element in the array")
# brute force way :- O(nlogn)
nums = [55,32,97,99,3,67,2,6,5]

nums.sort()
n = len(nums)
print(nums[n-2])


nums = [55,32,97,99,3,67,2,6,5]
# some nice way 

largest = float("-inf")
s_largest = float("-inf")
n = len(nums)
for i in range(0,n):
    largest = max(largest, nums[i])

for i in range(0,n):
    if nums[i] > s_largest and nums[i] != largest :
        s_largest = nums[i]

print(s_largest)

nums = [55,32,97,-55,3,67,2,6,5]
largest = float("-inf")
s_largest = float("-inf")

for i in range(0,n):
    if nums[i] > largest:
        s_largest = largest 
        largest = nums[i]

    elif nums[i] > s_largest and nums[i] != largest :
        s_largest = nums[i]

print(s_largest, "correct")

# the above both way have same tc

print("\n lec-26\n")
"""
Lecture 26 :- check of the array is sorted
"""
nums = [55,32,97,-55,3,67,2,6,5]
n = len(nums)

for i in range(n-1):
    if nums[i] > nums[i+1]:
        print("false")

"""
Lecture 27 :- Removes duplicates from sorted array 
"""
nums = [1,1,1,2,3,4,4,7,9,9,9,10]
freq_map = {}
n = len(nums) # 12 
for i in range(n):
    freq_map[nums[i]] = 0 
# for i in range(n+1):
#     freq_map[nums[i]] = 0    -> this is wrong 

j = 0

for k in freq_map :
    nums[j] = k
    j+=1
print(j)
# print(new)


print("\n\n lec 28 :- another lore\n\n")
"""
lecture 28 :- rotate array by 1 then we will see the rotaion of the array by k element leetcode question 
"""
# 1 st way is slicing 
nums = [1,2,3,4,5,6,7,8]
n = len(nums)
nums[:] = [nums[-1]] + nums[0:n-1]
print(nums)

nums = [1,2,3,4,5,6,7,8]
# 2nd method is reverse loop
n = 8 
temp = nums[-1]
for i in range(n-2,-1,-1) :
    nums[i+1] = nums[i]
nums[i] = temp
print(nums)

"""
lecture 29 :- rotate array by k element 
"""
# brute force way 
nums = [3,9,5,6,7,2]
n = len(nums)
k = 3
for i in range(k):
    temp = nums[-1]
    for j in range(n-2,-1,-1):  # -1 mtlb first element tk jaega aur third wala -1 mtlb ulta jaega 
        nums[j+1] = nums[j]
    nums[0] = temp 
print(nums)

# also do it by slicing method
nums = [3,9,5,6,7,2,10,9]
k = 5
n = len(nums)
nums[:] = nums[n-k:] + nums[0:n-k]
print(nums) 

# the optimal solution 
nums = [3,9,5,6,7,2,10,9]
k = 5
def reverse(nums,left,right) :
    while left < right :
        nums[left], nums[right] = nums[right], nums[left]
        left+=1
        right-=1
reverse(nums,n-k, n-1)  # 3,9,5,9,10,2,7,6
reverse(nums,0,n-k-1)   # 5,9,3,9,10,2,7,6
reverse(nums,0,n-1)     # 

print(nums)


"""
lecture :- 30 move zeroes to the end :- two pointer solution
"""

"""
lecture :- 31 :- implementing linear search 
"""
nums = [1,2,44,5,7,6,5]
target = 5 

n = len(nums)
for i in range(n):
    if nums[i] == target :
        print(i)


"""
lecture :- 32
"""
nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]
result = []
n,m = len(nums1), len(nums2)
i,j = 0,0

while i < n and j < m :
    if nums1[i] <= nums2[j] :
        if len(result) == 0 or nums1[i] != result[-1] :
            result.append(nums1[i])
        i+=1    
    else :
        if len(result) == 0 or nums2[j] != result[-1] :
            result.append(nums2[j])
        j+=1
if i < n :
    while i < n :
        if len(result) == 0 or nums1[i] != result[-1] :
            result.append(nums1[i])
        i+=1
if j < m :
    while j< m :
        if len(result) == 0 or nums2[j] != result[-1] :
            result.append(nums2[j])
        j+=1
print(result)

"""
lecture :- 33 -> find the missing value  ----- >lc
"""
nums = [9,6,4,2,3,5,7,0,1]
freq = {}
n = len(nums)
for i in range(n):  # this is the normal you are creating not of the nums
    freq[i] = 0
for num in nums :
    freq[num] = 1

for k,v in freq.items() :
    if v == 0 :
        print(k)

nums = [9,6,4,2,3,5,7,0,1]
# optimal way 
def missing(nums) :
    n = len(nums)  # 9 
    tot,sums = 0,0
    for i in range(n+1):
        sums = sums + i
    for i in range(n):
        tot = tot + nums[i]

    return sums - tot
print(missing(nums))
