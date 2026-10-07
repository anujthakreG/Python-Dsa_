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
Lecture 26 :- check if the array is sorted
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
reverse(nums,n-k, n-1)  # 3,9,5,9,10,2,7,6    because we have to pass the index value 
reverse(nums,0,n-k-1)   # 5,9,3,9,10,2,7,6
reverse(nums,0,n-1)     # 

print(nums)


"""
lecture :- 30 move zeroes to the end :- two pointer solution
"""
from typing import List
class MoveZero :
    def move(self, nums : List[int]) -> None:
        # we have to keep two pointers start and i 
        start = 0  # start is for keeping 
        n = len(nums)

        for i in range(n):   # starts from the 0 ,,,,,,,,,,,,,0 se n-1
            if nums[i] !=0 :
                # swap it if it is non zero element 
                nums[i], nums[start] = nums[start], nums[i]
                start+=1
            # return []
m1 = MoveZero()
nums = [0,1,0,3,12]
# nums = [1,2,0,3,12]
# print(m1.move(nums))   -> was not working
m1.move(nums)
print(nums)

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


"""
lecture 34  :- count the max consecutive ones 
"""

nums = [1,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1]
def maxcount(nums) :
    n = len(nums)
    count = 0 
    max_count = 0
    for i in range(n):
        if nums[i] == 1 :
            count+= 1
        else :
            max_count = max(count,max_count)
            count = 0
    return max(count,max_count)

print(maxcount(nums))

"""
lecture 35 :- two sum probelm  -----> lc 
"""

# brute force way 
nums = [5,9,1,2,4,15,6,3]
target = 13
# y = 0
n  = len(nums)
for i in range(n):
    x = target - nums[i]
    for j in range(i+1,n):
        if nums[i] + nums[j] == target :
            print(i,j)

def optimal(nums) :
    hash_map = {}
    n = len(nums)
    for i in range(n) :
        rem  = target - nums[i]
        if rem in hash_map :
            return [hash_map[rem], i]
        hash_map[nums[i]] = i     # here the key:value pair is like this :- key(nums element)  : value(index value of the element)
print(optimal)


"""
lecture 36 :- find the max subarray   
"""

# also known as kadanes algo
nums = [-2,1,-3,4,-1,2,1,-5,4]
total = 0 
n = len(nums)
maxi = float("-inf")
for i in range(n):
    total = total + nums[i]
    maxi = max(total,maxi)

    if total < 0 :
        total = 0
print(maxi)

print("| l37 |  ")
"""
lecture 37 :- best time to buy and sell stock -> lc 121
"""
price = [7,2,1,5,6,4,8]
n = len(price)
max_p = 0 
for i in range(n):
    for j in range(i+1,n):
        if price[j] > price[i]:
            p = price[j] - price[i]
            max_p = max(max_p,p)
print(max_p)   # -> this was the brute force way to find the solution with the tc of o(n^2)

# the optimal solution 
price = [7,2,1,5,6,4,8]               # we will see it again by doing the dry run of the code 
min_price = float("-inf")
max_price = 0 
n = len(price)
for i in range(n):
    min_price = min(min_price, price[i])
    max_price = max(max_price, price[i] - max_price)
print(max_price)


"""
lecture 38 :- rearrange array elements by sign  --> lc 2149 
"""

nums  = [5,10,-3,-1,-10,6]
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


print("\n | largest consecutive sequence ")
"""
lecture 39 :- largest consecutive sequence          -> lc 128 
"""

# 1 brute force way with a tc of o(n^2)
nums = [1,99,101,98,2,5,3,100,1,1]
n = len(nums)
max_count = 0
for i in range(n):
    num = nums[i]
    count = 1
    while (num+1) in nums:   # this is like jab tk num+1 nahi milega it will iterate from the start to thr end 
        count+=1
        num = num+1
    max_count = max(count,max_count)

print(max_count)


# 2 -> better way    -> we have to use last_smaller number here 
nums = [1,99,101,98,2,5,3,100,1,1]
n = len(nums)
# nums = nums.sort()    # this will return the value none just simply write
nums.sort()
# then the nums will be :- [1,1,1,2,3,5,98,99,100,101]   -> we sorted this just becasue that we dont have to iterate the entire nums again and again
count = 0
last_smaller = float("-inf")
longest = 0 
for i in range(n):
    num = nums[i]
    if num-1 == last_smaller:    # then this is the starting point 
        count += 1
        last_smaller = num
    elif num-1 != last_smaller :
        count = 1 
        last_smaller = num
    longest = max(longest, count)
print(longest)                        # -> tc is o(nlogn) + o(n)  :- sort + single loop 


# the optimal way of the solution  
nums = [1,99,101,98,2,5,3,100,1,1]
n = len(nums)
count = 0
"""
before proceding remember this :- d = {
    "a": 10,
    "b": 10,
    "c": 20
}              in dict keys are unique but the values may be common

and in set all elements are unique 
"""
my_set = set()
for i in range(n):
    my_set.add(nums[i])
longest = 0
for num in my_set:
    if num-1 not in my_set :  # that means this is the starting point 
        x = num 
        count = 1
        while x+1 in my_set :
            count+=1
            x+=1
        longest = max(longest,count) # ---> this is the optimal solution with tc of o(n+n+n)  the this n is a bit tricky :- look carefully while reading the while loop
print(longest)
# so it has a tc good then the better solution 


"""
lecture 40 :- learn about 2d list or matrix 
"""
"""
this is how you create a empty matrix of 0's with n rows and m col
"""
# n = 3
# m = 4

# mat = [[0 for _ in range(m)] for _ in range(n)]


# how to represent in 2d list 
nums = [[5,20,3], [7,-10,9], [1,-52,6]]
rows = len(nums)
col = len(nums[0])
# i is for rows and j is for coloumns
for i in range(0,rows):
    for j in range(0,col):
        print(nums[i][j],end = " ")
    print( )

print("print upper triangle")
# 1> print upper triangle
nums = [[5,10,8], [7,6,3], [2,1,9]]
rows = len(nums)
col = len(nums[0])
for i in range(0,rows):
    for j in range(0,col):
        if j >= i:
            print(nums[i][j], end = " ")
        else :
            print("*", end = " ")
    print()


print("lower triangle")
nums = [[5,10,8], [7,6,3], [2,1,9]]
rows = len(nums)
col = len(nums[0])
for i in range(0,rows):
    for j in range(0,col):
        if j <= i:
            print(nums[i][j], end = " ")
        else :
            print("*", end = " ")
    print()


print("diagonal triangle")
nums = [[5,10,8], [7,6,3], [2,1,9]]
rows = len(nums)
col = len(nums[0])
for i in range(0,rows):
    for j in range(0,col):
        if j == i:
            print(nums[i][j], end = " ")
        else :
            print("*", end = " ")
    print()

# i,j = 
# 0,1  
# 1,0
nums = [[5,8,9], [10,7,6], [3,1,2]]
rows = len(nums)
col = len(nums[0])
result = [[0] * rows for _ in range(col)]       # what is the meaning of this :- _
for i in range(rows):
    for j in range(col):
        result[j][i] = nums[i][j]
print(result)
"""for i in range(n):    # --> this is the second way of doing the transpose of the matrix 
    for j in range(i+1,n):
        nums[i][j], nums[j][i] = nums[j][i], nums[i][j]"""   # -> another waay to do the transpose of the matrix
# same for 2*3 matrix


"""
lecture 41 :- set matrix zero 
"""
# brute force way :- 
nums = [[7,9,2,3], [20,8,0,10], [20,0,-10,5], [4,14,6,7]]

class Solution:
    def markinfinity(self, matrix,row,col) :
        r = len(matrix)
        c = len(matrix[0])
        for i in range(0,r) :
            if matrix[i][col] != 0 :
                matrix[i][col] = float("-inf")
        for j in range(0,c):
            if matrix[row][j] != 0 :
                matrix[row][j] = float("-inf")

    def setzeroes(self, matrix) -> None:

        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    self.markinfinity(matrix, i, j)
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == float("-inf"):
                    matrix[i][j] = 0 
S1 = Solution()
S1.setzeroes(nums)
rows = len(nums)
col = len(nums[0])
for i in range(0,rows):
    for j in range(0,col):
        print(nums[i][j],end = " ")
    print( )

# optimal way to use the stack where we will mark -1 both in teh row and col stack when ever there will be 0 
print("optimal way to print the set zero matrix ")
nums = [[7,9,2,3], [20,8,0,10], [20,0,-10,5], [4,14,6,7]]
r = len(nums)
c = len(nums[0])

row_track = [0 for _ in range(r)]
col_track = [0 for _ in range(c)]

# row_track = [0] * r
# col_track = [0] * c


for i in range(r):
    for j in range(c):
        if nums[i][j] == 0 :
            row_track[i] = -1
            col_track[j] = -1
for i in range(r):
    for j in range(c):
        if row_track[i] == -1 or col_track[j] == -1 :
            nums[i][j] = 0 

for i in range(r):
    for j in range(c) :
        print(nums[i][j], end = " ")
    print()


print("| lecture 42 |")
"""
lecture 42 :- rotate the matrix by 90 degrees :-           lc 48
"""

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
r = len(nums)
c  = len(nums[0])

# first take the transpose then swap it 
result = [ [0]* r for _  in range(c)]
for i in range(r):
    for j in range(c):
        result[j][i] = nums[i][j]

"""
1 5 9 13 
2 6 10 14 
3 7 11 15 
4 8 12 16
"""

for i in range(r):
    k = 0 
    j = 3 
    while k <= j :
        result[i][k], result[i][j] = result[i][j], result[i][k]
        k+=1
        j-=1

for i in range(r):
    for j in range(c) :
        print(result[i][j], end = " ")
    print()

# now this code is not optimal as we are creating a different matrix to solve the problem , so :- tc == sc = o(n*m)

print("optimal solution :- ")
# the optimal solution :- 
nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

n = len(nums)
r = len(nums)
c  = len(nums[0])
# just simply transpose the matrix :- 
for i in range(n):    # --> this is the second way of doing the transpose of the matrix 
    for j in range(i+1,n):
        nums[i][j], nums[j][i] = nums[j][i], nums[i][j]


for i in range(n):
    nums[i].reverse()

for i in range(r):
    for j in range(c) :
        print(nums[i][j], end = " ")
    print()


"""
lecture 43 :- print the matrix in spiral order :-           --->lc 54
"""

matrix = [
    [1,  2,  3,  4,  5,  6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11]
]

result = []
def spiralprint(matrix):
    top,left = 0,0
    right, bottom = len(matrix[0]) - 1 , len(matrix) - 1 
    while top <= bottom and left <= right :
        for i in range(left, right+1) :
            result.append(matrix[top][i])
        top+=1
        for i in range(top, bottom + 1) :
            result.append(matrix[i][right])
        right-=1

        if top <= bottom :  # this two conditions are main i.e. tricky 
            for i in range(right, left -1 , -1):
                result.append(matrix[bottom][i])
            bottom-=1

        if left<= right :
            for i in range(bottom, top-1,-1) :
                result.append(matrix[i][left])
            left+=1
    return result
print(spiralprint(matrix))


print("\n 3sum :- \n")
"""
lecture 44 :- 3sum problem           ---> lc 15 
here continue will simply +=1 not run the below code
and break means it will stop from that position
"""



# brrute force way of the solution   -> tc = o(n3)  and sc -> O(no of triplets)
arr =  [-1,0,1,2,-1,4]
n = len(arr)
my_set = set()
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i] + arr[j] + arr[k] == 0 :  # always remember you cannot add a list in the set :- beacuse list is not a hashable type but yes you can add a tuple in the list
                temp = [arr[i], arr[j], arr[k]]
                temp.sort()
                my_set.add(tuple(temp))   # that is why we added tuple in the set 

ans = [list(ans) for ans in my_set ]  # then we used list comprehension in the final answer 
print(ans)


# always remember to find any element in the liost/array better way is to use dict or set
def better(nums) :    # tc : o(n2) , sc :- O(n) + O(No. of triplets)
    result = set()
    n = len(nums)
    for i in range(n):
        my_set = set()
        for j in range(i+1,n):
            k = -(nums[i]+nums[j])
            if k in my_set :
                temp = [nums[i],nums[j],k]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[j])
    return result

arr =  [-1,0,1,2,-1,4]
print(better(arr))

def optimal(nums):
    n = len(nums)
    nums.sort()
    result = []
    for i in range(n):
        if  i!= 0 and nums[i] == nums[i-1] :
            continue    # means it will simply do i+=1 and the below written code will not return this is the code to ignore the value of repeated i 

        j = i + 1
        k = n-1
        while j < k :
            total = nums[i] + nums[j] + nums[k]
            if total < 0 :   # apn ko 0 ke close ya o tk pohochna hai , here we can say 0 is the target value
                j+=1
            elif total >0 : 
                k-=1
            else : # means here you got the total = 0 
                temp = [nums[i],nums[j],nums[k]]
                result.append(temp)
                j+=1
                k-=1
                # now the new j and k value should not be equal to the prev appended j and k value so new conditions 
                # we are not using any dict/freq here 
                while j < k and nums[j] == nums[j-1]:
                    j+=1
                while j < k and nums[k] == nums[k+1] :
                    k-=1
    return result 
nums = [-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
arr =  [-1,0,1,2,-1,4]
print(optimal(arr))
print(optimal(nums))

# this is the optimal solution for the 3sum problem with TC = O(N logn ) + O(n2), sc :- O(no. of triplets)

"""
lecture 45 :- 4sum problem           ---> lc 18
"""

def brute(nums) :
    n = len(nums)
    my_set = set()
    res = []
    for i in range(n):
        for j in range(i+1,n) :
            for k in range(j+1,n) :
                for l in range(k+1,n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == 0 :
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
    return [list(ans) for ans in my_set]

nums = [1,0,-1,0,-2,2,5,9]
print(brute(nums))

nums = [1,0,-1,0,-2,2,5,9]
def optimal(nums,target) :
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n) :
        if i != 0 and nums[i] == nums[i-1] :
            continue # just ignore
        for j in range(i+1,n) :
            if j > i+1 and nums[j] == nums[j-1] :
                continue
            k = j+1
            l = n-1

            while k < l :
                total = nums[i] + nums[j] +nums[k] +nums[l]
                if total == target :
                    temp = [nums[i],nums[j],nums[k],nums[l]]
                    result.append(temp)
                    k+=1
                    j-=1
                    while k < l and nums[k] == nums[k-1] :
                        k+=1
                    while k < l and nums[j] == nums[j+1] :
                        j-=1

                elif total < target :
                    k+=1
                else :
                    l-=1
    return result

nums = [1,1,1,1,2,2,3,3,3,4,4,4,5,5]
print(optimal(nums,8))

# tc :- O(n3) here nlogn is ignored because it is very less then n3 and sc :- o(1) == o(no of triplets) 
"""
lecture 46 :- binary search       -> very very imp for binary search for interview 
beacuse it usually gives the optimal silution in most of the cases 
"""

# it is used to reduce the tc of the solution :- 
nums = [2,4,6,7,9,11,18,19]
# this is the iteratve approach
def binarys(nums,target) :    # -> O(logbase2N)  , sc :- O(1)
    low,high = 0,len(nums) - 1

    while low <= high :
        mid = (low+high) // 2 
        if nums[mid] == target :
            return mid
        elif target > nums[mid] :
            low = mid + 1
        else :
            high = mid - 1
    return -1 
print(binarys(nums, 11))
# this is the recursive approach



"""
lecture 47 :- upper and lower bound 
"""
# lower bound :- smallest index such that nums[i] >= target , we have to returnt the index of the target element 
# in the searching if the target ele is not present then return -1
def lb(nums) :
    n = len(nums)
    lb = -1
    low,high = 0, n- 1
    while low <= high :
        mid = (low+high) // 2 
        if nums[mid] >= target:
            lb = mid
            high = mid-1
        else :
            low = mid + 1  #apn ko low tk jana hai islioye yaha lb ki condition nahi likhi kyuki age jake low wala hi lb banega
    return -1

# upper bound :- smallest index such that nums[i] > target 

# in the searching if the target ele is not present then return -1
def ub(nums) :
    n = len(nums)
    ub = n   # this condition also wokrs for lb 
    low,high = 0, n- 1
    while low <= high :
        mid = (low+high) // 2 
        if nums[mid] > target:
            ub = mid
            high = mid-1
        else :
            low = mid + 1 
    return -1


"""
lecture 48 :- search insert position :-    --> lc 35 
"""
nums = [1,3,4,5,8,9,14,15,19,20,21]
# simply it is the case of lb



"""
if you have to reduce the tc from O(n) more then O(n) -> O(logn)  this is more precise
"""
"""
lecture 49 :- floor and ceil in sorted array :- 
"""
# ceil :- smallest number in the array >= target
# floor :- largest number in the array <= target
# [floor,  ceil]    -> if th values not exists then return -1 to that paticular 


# this nums is already sorted :- 
nums = [3,4,4,4,8,9,9,10,12,12,14,15]   # this is the optimal solution 
def cf(nums,target) :
    n = len(nums)
    ceil, floor = -1,-1
    low,high = 0,n-1
    while low <= high :
        mid = (low+high) // 2 
        if nums[mid] == target :
            return [nums[mid], nums[mid]]
        elif nums[mid] > target :
            ceil = nums[mid]  # you have to store the value not the index
            high = mid-1
        else :
            floor = nums[mid]
            low = mid+1
    return (floor, ceil)

print(cf(nums,6))


"""
lecture 50 :- find fisrt and last occurence in the sorted array :-      --> lc 34
"""

def brute(nums,target):
    f,l = -1,-1
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            if f == -1:
                f = i
            l = i 
    return (f,l)
nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target = 3
print(brute(nums,target))

# what is the more precise tc then O(n) :
# just club the solution of both the lower and upper bound in one solution :-  it will be the optimal solution for this question 

"""
lecture 51 :- count occurences in the sorted array
"""
nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]

def brute(nums,target) :
    n = len(nums)
    first, last = -1,-1
    for i in range(n) :
        if nums[i] == target :
            if first == -1 :
                first = i 
            last = i 
    if first == -1 :
        return -1 
    return (last-first)+1
print(brute(nums,3))   # same goes as above for the oprimal solution for this question

"""
lecture 51 :- search in rotated sorted array     --> lc 33
"""
nums = [1,4,5,6,8,9,10,11,15,20]
def sra(nums,target) :
    n = len(nums)
    low,high = 0, n-1
    while low <= high :
        mid = (low+high) // 2 
        if nums[mid] == target :
            return mid
        elif nums[mid] > target :
            ceil = nums[mid]
            high  = mid-1
        else :
            floor = nums[mid]
            low = mid+1
    return - 1
print(sra(nums,6))
print(sra(nums,13))

"""
lecture 53 :- search in rotated sorted array II     ---> lc 81 
"""
nums = [10,11,11,12,12,13,13,13,1,2,3,4]
def brute(nums,t) :
    n = len(nums)
    for i in range(n):
        if nums[i] == t :
            return True
        else :
            False
print(brute(nums,11))

# 53 and 54 remaining 

"""
lecture 55 :- Starting with the linked list 

"""

"""
lecture 56 :- Starting with the linked list 
"""
class Node :
    def __init__(self,val):
        self.val = val
        self.next = None
# what are methods inside a class
# rets we all know the operations if any refer to old file


"""
lecture 57 :- Middle of the linked list      --> 876
"""
# refer this list as linke dlist
nums = [5,10,27,3,99]
def brute(self,nums) :
    n = 0 
    temp = self.head
    while temp != None :
        temp = temp.next
        n+=1
    for i in range(n // 2 ):
        temp = temp.next
    return temp

# optimal solution can be the slow and fast pointer 
# where when fast.next is None then slow will be at the mid position 


# classical stucture for the linked list :- 
class Node :
    def __init__(self, val):
        self.val = val 
        self.next = None

"""
lecture 59 :- linked list cycle , Floy'd cycl detection      --> lc 141 
""" 
#--> solution done in lc 


"""
lecture 60 :- find the cycle starting point    --> lc 142
""" 
# solution in the lc just return the repeated node you find again the set 

"""
lecture 61 :- find length of the loop in the cycle 
""" 
def lengthcycle(head) :
    slow, fast = temp, temp 
    while fast is not None and fast.next is not None:  # this will be the favourable cindition for both the ccycle and non cycle case
        fast = fast.next.next  
        slow = slow.next

        if slow == fast :
            l = 1 
            fast = fast.next
            while fast != slow :
                fast = fast.next
                l+=1
            return l
    return -1 


"""
lecture 62 :- odd even linked list
"""

"""
When you delete a node:

temp.next = temp.next.next
"""
# tried but dk how to reassrange the ll
def brute(head) :
    temp = head
    values = []
    # while temp != None  # this will be not the goodd conditions as it will not be able to append the value at full
    while temp and temp.next : # mtlb ye jab tk ho rha hai
        values.append(temp.val)
        temp = temp.next.next
    temp = head.next 
    while temp and temp.next : # mtlb ye jab tk ho rha hai
        values.append(temp.val)
        temp = temp.next.next
    ind = 0
    temp = head
    while temp != None :
        temp.val = values[ind]
        ind+=1
        temp = temp.next
    return head  # so this solution has tcof o2n and sc of on

def optimal(head) :

    # in this solution we just changs the links not updated the values 
    # edge case :
    if head is None or head.next is None :
        return head 
    odd = head
    even = head.next 
    even_head = even
    # try to find some thing very common for the solution like this  :- 
    while even != None and even.next != None :
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next 
    odd.next = even_head
    return head # this solutino has tc of O(n/2) and sc of O(1)


"""
lecture 63 :- remove nth node from the end of the linked list
"""

def removen(head,n) :  # this is the brute force solution 
    temp  = head
    c = 0
    while temp != None :
        temp = temp.next
        c+=1
    if c == n :
        new_head = head.next
        return new_head 
    t = c - n 
    for i in range(t) :
        temp = temp.next
    temp.next = temp.next.next

    return head 

def optimal(head,n) :
    temp = head
    slow = head

    for i in range(n) :
        fast = fast.next
    if fast == None :
        return head.next
    
    while fast.next != None :
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head 

"""
lecture 64 + 65 :- starting with the doubley linked list 
"""
class Node :
    def __init__(self,val):
        self.val = val 
        self.next = None
        self.prev = None

class Doublulinkedlist :
    def __init__(self) :
        self.head = None

    # 1 inserting a position at head
    def insert_at_head(self,val) :
        New_node = Node(val)
        if not self.head :
            self.head = New_node
        else :
            New_node.next = self.head
            self.head.prev = New_node
            self.head = New_node 

    # 2 append (add at last)
    def append(self,val) :
        new_node = Node(val)
        if not self.head :
            self.head = new_node
        else :
            current = self.head
            while current != None :
                current = current.next
            current.next = new_node
            new_node.prev = current

    # 3 insert at specific position 
    def insert_at_pps(self,val,position):
        new_node = Node(val)
        if position == 0 :
            self.insert_at_head(val)
            return 
        
        current = self.head
        count = 0 
        while current and count < position - 1 :
            current = current.next
            count+=1
        if current is None :
            print("position out of bounds !")
            return 
        new_node.next = current.next
        new_node.prev = current
        if current.next :
            current.next.prev = new_node
        current.next = new_node

"""
lecture 66 :- reverse a doubly linked list :- 
"""
# the optimal solution
def revers(head):
    if head.next is None :
        return head
    curr = head
    prev = None
    while curr is not None :
        front = curr.next
        curr.next = prev
        curr.prev = front
        prev = curr
        curr = front
    return prev # this are all the o(1) operaions


# 67,68,69 -> do it remaining


"""
Bit manipulation :- lec 70 
"""
# 1> how to convert integer to binary 

def convert2binary(num:int)->str:
    result = ""
    while num > 0 :
        if num%2 == 1 :
            result+="1"
        else :
            result+="0"
        num = num // 2   # here we are dividing the numrbe with 2 , therefore base = 2 
    result = result[::-1]   # by slicing we will reverse the number 
    return result
print(convert2binary(13))    # tc :- O(logbase n)

# 2> how to convert binary to decimal (int)
def convert2decimal(x:str) -> int :
    decimal_num = 0 
    power = 0
    index = len(x)-1
    while index >= 0 :
        num = int(x[index]) * (2 ** power)
        decimal_num+=num
        power+=1
        index-=1

    return decimal_num

def convert2decimall(x:str) -> int :   # my pov 
    decimal_num = 0 
    power = 0
    index = len(x)-1
    for i in range(index, -1,-1):
        num = int(x[i]) * (2 ** power)
        decimal_num+=num
        power+=1
        # index-=1

    return decimal_num
x = "1101"
print(convert2decimall(x))            # TC :- O(len)

""" 
how deos the computer store the bits :- 
if x = 13 then deci to binary :- 1101 and rest of the 28 bits are 0's so 28 + 4 = 32 bits 
and we wanto print the x then ii will convert the binary to decimal
"""

"""
1's : convert the deci to binary and then flip the digits 
and
2's compliment : convert it to 1's compliment and then add 1 to it 
"""

#-------------------------------------------------------------------------
"""
different types of operator : and , or , xor, not, shift 

1> AND  :- all true -> true || one false -> false
2> OR :- one true -> ture || all false -> false 
3> XOR x^y :- same :- false(0) || different -> true(1)
           :- if no of 1's is odd -> 1 , no of 1's is even -> 0 
4> SHIFT x >> 1(right shift)
         :- 1101 > 1 :- 0110  :- x / 2^k 

         x << 1 (left shift)
5> NOT operator :- checks whether -ve or not -> sign ~
    do the 2's compliment 
    flip the number 
    check the first leftmost bit of the number it is -ve or not -> if not stop else do 2's 
    0 means it is not negative

    ex:- x = ~(-13) = 12 
"""


"""
lecture 71 :- Bit Manipulation Basics | Swapping, Setting, Clearing, Toggling Bits
"""

# swapping 
a = 5 
b = 10 
print("initial, a :- ",a , "b :-",b)
a = a^b
b = a^b  # here b becomes a 
a = a^b  # here a becomes b 

print("a :- ",a, "b :- ",b)


# check if the ith bit is set or not ,if the ith number is 1 or not 
"""
1> do the left shift of 1 by the ith number , and then do the and operation :- if it comes to be true the ith posiition then the bit is set
"""
print("uaing left shift :")

N = 13
i= 2
if (N &(1<<i)) != 0 :
    print("True")
else :
    print("False")

"""
2> by using right shift n >>1 , AND operation with 1
"""
print("using right shift :")
N = 13
i = 2 
if (N >> i & 1) != 0 :
    print("True")
else :
    print("False")


# set the ith bit :- if the given index is 0 
N = 9 
i = 2
a = (N | 1<<i)  # we are using OR here to maintain the other bits same 
print(a)


# clear the ith bit :- to make it 0 if he ith bit is 1 , and to do nothing if it is already 0 
N = 13 
i = 2 # i will be always given to you , the ith bit
b = (N & ~(1<<i))
print(b)


# toggle the ith bit 
N=13
i= 2
c = N ^ 1<<i  # using the xor operator 
print(c)


# remove the rightmost bit i.e convert 1 to 0 (rightmost)
N = 13 # 1101 -> 1100 we can i iterate from right to left 

nn = list("1100")
n = len(nn) - 1
c = 0 
for i in range(n,-1,-1):
    if nn[i] == "1" and c < 1 :
        nn[i] = "0"
        c+=1
print(nn)  # but we have to convert it to list 

# below is the optimal solution :- 
N = 16
d = (N & N-1)
print(d)

N = 40
d = (N & N-1)
print(d)

# check if the number is power of 2 
N1 = 8
N2 = 7
def cck(N):
    if (N & (N-1)) == 0 :
        return True
    else :
        return False
print(cck(N1))
print(cck(N2))


"""
lecture 72 :- Minimum bit flips to convert number     -> lc 2220
"""
start = 3
goal = 4
ans = start ^ goal
count = 0 
for i in range(0,32):
    if ans&(1<<i) != 0 :
        count+=1
print("number of changes required :- ",count)     # TC :- O(32) if wanto to decrease it then do the logbase2N solution n= n //2 

"""
lecture 73 :- Bit manipulation and Xor trick     -> lc 136
"""

# the brute force solution witout the bit manipulation 
nums = [5,1,3,3,7,1,7]
freq = {}
n = len(nums)
for i in range(n):
    if nums[i] not in freq :
        freq[nums[i]] = 1
    else :
        freq[nums[i]]+=1
for k,v in freq.items():
    if v == 1 :
        print(k)

ans = 0
for num in nums :
    ans = ans^num
print(ans)

"""
lecture 74 :- Generate Subsets Using Bit Manipulation
"""

# 2 power n -> is same as 1<<n

nums = [1,2,3]
n = len(nums)
total_subsets = 1<<n  
result = []
for num in range(total_subsets):
    lst = []
    for i in range(n):
        if num & (1<<i) != 0 :
            lst.append(nums[i])
    result.append(lst)
print(result)


"""
lecture 75 :- Advanced recursion -> v.v.v imp -> all the below things are imp for backtracking 
"""

# before starting you should know this topics :- 
"""
1> Print all the subsequences
2> Find all subsequences with sum = k 
3> check if there exists a subsequence with sum = K
4> Count all subsequences with Sum = K
"""

# sunsequence -> continours/ non-continous sequence which follows the order 
# subarrays are continous where as subsequence are both continous and non continous but in a specific direction   Example nums = [1,2,3,4,5] -> [1,2,3] and [1,3,4]
nums = [5,7,9]
result = []
def func(index,subset) :
    if index >= len(nums):
        result.append(subset.copy())
        return 
    subset.append(nums[index])
    func(index+1,subset)
    subset.pop()
    func(index+1,subset)
func(0,[])
print(result)


"""
lecture 76 :- Generate Subsequences with Sum K 
"""

# brute force :- we can also use the above solution also
nums = [5,9,4]
result = []
target = 9
def func(index,subset) :
    if index >= len(nums):
        if sum(subset) == target :
            result.append(subset.copy())
        return  
    subset.append(nums[index])
    func(index+1,subset)
    subset.pop()
    func(index+1,subset)
func(0,[])
print(result)


"""
to solve this type of questions :- 
-> first do the dry run of the code note down all of the steps 
-> then write down the coe , and return will go to the caller function and continue executing the after codes 
"""
# the optimal solution :- 
nums = [5,9,4]
res = []
sum = 0 
def func(index, total ,subset) :
    if total == target :
        result.append(subset.copy())
        return
    elif total > target :
        return 
    if index >= len(nums) :
        return 
    subset.append(nums[index])
    sum = total + nums[index]
    func(index+1,sum, subset)
    e = subset.pop()
    sum = sum - e 
    func(index+1,sum, subset)

""""
lecture 77 :- check if there exists a subsequence with sum = k 
"""
# you just have to check whether there is one sequence only or not 

def func(index,total,subset) :
    if total == target :
        result.append(nums[index])
        return True
    elif total > target :
        return False
    if index >= len(nums) :
        return False
    subset.append(nums[index])
    sum = sum + nums[index]
    pick = func(index+1,sum,subset)
    if pick == True :   # this is beacause if it finds the soliution before then no need to sun the below code of lines 
        return True 
    subset.pop()
    sum = total
    not_pick = func(index+1,sum,subset)
    return not_pick

"""
lecture 78 :- Count All Subsequences with Sum K    -> remaining 
"""

# def func(index, total , subset) :
#     if total == k :


"""
lecture 79 :-  Generate All Binary Strings , but there at the left or right of that index /1 there should not be 1
"""









"""
lecture 80 :- Generate parantheses  --> lc 22    -> striver and neetcode imp

according to the n there should be the n*2 parantheses
"""
n = 2 
result = []
brackets = [""] * (n*2)

def func(index,total,brackets,result) :
    if index >= len(brackets) :
        if total == 0 :
            result.append("".join(brackets))
        return 
    if total > len(brackets) // 2 : # or (n*2) // 2
        return 
    elif total < 0 :
        return 
    brackets[index] = "("
    Sum = total + 1
    func(index+1, Sum ,brackets, result)
    brackets[index] = ")"
    Sum = total - 1 
    func(index+1, Sum,brackets, result)


func(0, 0, brackets, result)
print(result)

