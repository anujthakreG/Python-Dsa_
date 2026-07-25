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

# example :- 1 to N 

# head print 1 to n :- mai pehele apni job kr rha hu fir function ko call kr rha hu 
# tail recurrsion :- mai function pehle call krta hu fir pirnt krta hu  