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
    if num  % i == 0:
        result.append(i)
print(result)

# 2> better way -> tc :- o(n/2) almost similar to o(n)
n = 10
nums = n 
result = []
for i in range(1, (nums // 2) + 1):
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

# 2nd method :- hash map 
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
        return    # but in this type of return it goes to the function which called him
    nsum(sum+i,i+1,n)

nsum(0,1,10)

# but when you dont print but reutrn something that is called as functional recusrsion
print("functional recursion :- ")
n = 10 
def ffcun(n):
    if n == 1:
        return 1 # means that function will return 1 not the whole answer will be one , kuch likh ke return kro to it is called as functional recursion
    return n + ffcun(n-1)   # you directly return here only 
x = ffcun(10)
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
print("recursion based approach")     
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

def fib(n):
    if n == 0 or n == 1 :
        return n  # it will return the value upward 
    return fib(n-1) + fib(n-2)

n = 10 
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
lecture 22 :- merge sort , works on the principle of divide and conquoer 
"""