nums = [1,2,3,4,5,6,7,8,9]

# reversing an array using recurrsion

# practicing all the sorts :- 

#1> selection sort :- 
nums = [8,7,6,5,4,3,2,1]
def selection(nums) :
    n = len(nums)
    for i in range(n) :
        min_ind = i 
        for j in range(i+1,n):
            if nums[j] < nums[min_ind] :
                min_ind = j 
        nums[i], nums[min_ind] = nums[min_ind], nums[i]


nums = [55,32,97,99,3,67,2,6,5]
# find the largest and the second largest element in the array :-
def method(nums) :  # two loop method
    n = len(nums)
    larg = float("-inf")
    s_larg = float("-inf")
    for i in range(n):
        if nums[i] > larg :
            larg = nums[i]
    # at this position you will get the largest element 
    for i in range(n):
        if nums[i] > s_larg and nums[i] != larg :
            s_larg = nums[i]
    return larg, s_larg

print(method(nums))


def method2(nums) :  # this is the second method
    n = len(nums)
    larg = float("-inf")
    s_larg = float("-inf")
    for i in range(n) :
        if nums[i] > larg :
            s_larg = larg
            larg = nums[i]

        elif nums[i] > s_larg and nums[i] != larg :
            s_larg = nums[i]
    return larg, s_larg

nums = [55,32,97,99,3,67,2,6,5]
print(method2(nums))

nums = [1,1,1,2,3,4,4,7,9,9,9,10]
# remove duplicates from the sorted array 

def meme(nums1,nums2):
    
    result = []
    n,m = len(nums1), len(nums2)
    i,j = 0,0

    while i < n and j < m :
        if nums1[i] < nums2[j] :
            result.append(nums1[i])
            i+=1
        else :
            result.append(nums2[j])
            j+=1
    if i < n :
        while i < n :
            result.append(nums1[i])
            i+=1
    if j <m :
        while j < m :
            result.append(nums2[j])
            j+=1
    return result

nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]

print(meme(nums1,nums2))

# find the missing value ;
nums = [9,6,4,2,3,5,7,0,1]
def missing(nums) :
    n = len(nums)
    tot, sum = 0,0
    for i in range(n+1) :
        tot = tot+ i
    for i in range(n) :
        sum = sum + nums[i]
    return tot - sum 

print(missing(nums))



nums =  [-1,0,1,2,-1,4]
def three(nums) :
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n) :
        if i != 0 and nums[i] == nums[i-1] :
            continue

        j = i+1
        k = n-1 
        while j < k :
            tot = nums[i] + nums[j] + nums[k]
            if tot == 0 :
                temp = [nums[i], nums[j], nums[k]]
                res.append(temp)
                j+=1
                k-=1

                while j < k and nums[j] == nums[j-1] :
                    j+=1
                while j <k and nums[k] == nums[k+1] :
                    k-=1
            elif tot < 0 :
                j+=1
            else :
                k-=1
    return res

print(three(nums))

nums = [1,0,-1,0,-2,2,5,9]
def four(nums, target) :
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n) :
        if i != 0 and nums[i] == nums[i-1] :
            continue

        for j in range(i+1,n):
            if j > i +1 and nums[j] == nums[j-1] :
                continue

            k = j+1
            l = n-1

            while k < l :
                tot = nums[i]+nums[j]+nums[k]+nums[l]
                if tot == target :
                    temp = (nums[i],nums[j],nums[k],nums[l])
                    res.append(temp)
                    k+=1
                    l-=1

                    while k < l and nums[k] == nums[k-1] :
                        k+=1
                    while k < l and nums[l] == nums[l+1] :
                        l-=1
                elif tot < target :
                    k+=1
                else :
                    l-=1
    return res
print(four(nums,  0))
print(four(nums,  1))


4,3,2,7,8,2,3,1
4,3,2,7,8,2,3,1
nums = [4,3,2,7,8,2,3,1]
def h(nums) :
    n = len(nums)
    freq = {}
    for i in range(n) :
        freq[i] = 0
    
    for i in range(n) :
        if nums[i] not in freq:
            freq[nums[i]] = 1 
        else :
            freq[nums[i]] +=1
    for k,v in freq.items() :
        if v == 0 :
            print(k)

print(h(nums))


# ----------------------------------------------------
# satrting with the revision 
print("starting with the revision ")
# print the factorial of the number :- 

def fact(n) :
    if n == 0 or n ==1 :
        return n 
    return n * fact(n-1)
print(fact(5))

# s,b,i,m,q
print("selection sort :- ")

nums = [8,7,6,5,4,3,2,1,0]
def selection(nums) :
    n = len(nums)
    for i in range(n):
        min_ind = i 
        for j in range(i+1,n) :
            if nums[j] < nums[min_ind] :
                min_ind = j 
        nums[i] , nums[min_ind] = nums[min_ind], nums[i]
    return nums
print(selection(nums))

print("bubble")
nums = [8,7,6,5,4,3,2,1,0]
def bubble(nums) :
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1) :
            if nums[j+1] < nums[j] :
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
print(bubble(nums))

print("insertion")
nums = [8,7,6,5,4,3,2,1,0]
def insertion(nums) :
    n = len(nums)
    for i in range(n):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key :
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
    return nums

print(insertion(nums))


def merge_array(left,right) :
    i,j = 0,0
    n = len(left)
    m = len(right)
    res = []
    while i< n and j < m :
        if left[i] <= right[j] :
            res.append(left[i])
            i+=1
        else :
            res.append(right[j])
            j+=1
    if i < n :
        while i < n :
            res.append(left[i])
            i+=1
    if j < m  :
        while j < m :
            res.append(right[j])
            j+=1
    return res

def merge(nums) :
    if len(nums) <= 1 :
        return nums
    mid = len(nums) // 2 
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    left = merge(left_arr)
    right = merge(right_arr)
    return merge_array(left,right)

nums = [8,7,6,5,4,3,2,1,0]
print("merge")
print(merge(nums))


print("find the second largest :- ")
nums = [55,32,97,-55,3,67,2,6,5]
def findit(nums) :
    n = len(nums)
    larg = float("-inf")
    s_larg = float("-inf")
    # small = float("inf")
    for i in range(n) :
        if nums[i] > larg :
            s_larg = larg
            larg = nums[i]
        elif nums[i] > s_larg and s_larg != larg :
            s_larg = nums[i]
    return larg, s_larg
        
print(findit(nums))


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

price = [7,2,1,5,6,4,8]               # we will see it again by doing the dry run of the code 
min_price = float("-inf")
max_price = 0 
n = len(price)
for i in range(n):
    min_price = min(min_price, price[i])
    max_price = max(max_price, price[i] - max_price)
print(max_price)


print("print the marix by spiral order :- ")
# nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
nums = [
    [1,  2,  3,  4,  5,  6],
    [20, 21, 22, 23, 24, 7],
    [19, 32, 33, 34, 25, 8],
    [18, 31, 36, 35, 26, 9],
    [17, 30, 29, 28, 27, 10],
    [16, 15, 14, 13, 12, 11]
]
def spiral(nums) :
    top,left = 0,0
    res = []
    bottom, right = len(nums)- 1 , len(nums[0]) -1 

    while top <= bottom and left <= right :
        for i in range(left,right+1) :
            res.append(nums[top][i])
        top+=1
        for i in range(top, bottom+1) :
            res.append(nums[i][right])
        right-=1

        if top <= bottom :
            for i in range(right, left-1, -1):
                res.append(nums[bottom][i])
            bottom-=1

        if left<= right :
            for i in range(bottom, top-1, -1):
                res.append(nums[i][left])
            left+=1
    return res
print(spiral(nums))
        
print("3 sum :- ")
arr =  [-1,0,1,2,-1,4]

def optimalt(nums) :
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n) :
        if i != 0 and nums[i-1] == nums[i] :
            continue
        j = i+1
        k = n-1

        while j < k :
            tot = nums[i] + nums[j] + nums[k]
            if tot == 0 :
                temp = [nums[i], nums[j], nums[k]]
                res.append(temp)
                j+=1
                k-=1
                while j < k and nums[j-1] == nums[j] :
                    j+=1
                while j <k  and nums[k+1] == nums[k] :
                    k-=1
            elif tot < 0 :
                j+=1
            else :
                k-=1
    return res
print(optimalt(arr))

print("4 sum problem :- ")

# def optimalf(nums) :
#     n = len(nums)
#     nums.sort()
#     res = []
#     for i in range(n) :
#         if i!= 0 and nums[i-1] == nums[i] :
#             continue
#         for j in range(i+1,n) :
#             if j > i+1 and nums[j-1] == nums[j] :
#                 continue

#             k = j+1
#             l = n-1
#             while k < l :
#                 tot = nums[i]+nums[j]+nums[k]+nums[l]
#                 temp = [nums[i],nums[j],nums[k],nums[l]]           --> code hanged 
#                 res.append(temp)
#                 k+=1
#                 l-=1
#                 while k < l and nums[k] == nums[k-1] :
#                     k+=1
#                 while k < l and nums[l] == nums[l+1] :
#                     l-=1

print("the linked list :- ")

class Node :
    def __init__(self,val):
        self.val = val
        self.next = None

head = Node(1)
h2 = Node(2)
h3 = Node(3)
h4 = Node(4)
h5 = Node(5)
h6 = Node(6)
head.next = h2
h2.next = h3
h3.next = h4
h4.next = h5
h5.next = h6
h6.next = None

temp = head
while temp != None :
    print(temp.val, end = " ")
    temp = temp.next

def move(head):
    if head == None or head.next is None :
        return head 
    odd = head
    even_head = evem
    even = head.next
    while even is None and even.next is None :
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = even_head


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


nums = [1, -1, 3, 2, -7, -5, 11, 6 ]
def hh(nums) :
    n = len(nums)
    start = 0
    c = 0 
    for i in range(n) :
        if nums[i] <0 :
            nums[start], nums[i] = nums[i], nums[start]
            start+=1
            c+=1
    low = 0 
    high = n-1
   
    # return nums, c
print(hh(nums))

# [-1, -7, -5, 2, 1, 3, 11, 6]
nums = [1, -1, 3, 2, -7, -5, 11, 6 ]

class Solution:
    def move(self, nums,low,high) :
        while low < high :
            nums[low], nums[high] = nums[high], nums[low]
            low+=1
            high-=1
            
    def segregateElements(self, nums):
        # code here
        n = len(nums)
        start = 0
        c = 0 
        for i in range(n) :
            if nums[i] <0 :
                nums[start], nums[i] = nums[i], nums[start]
                start+=1
                c+=1
            # return nums, c
        # self.move(nums, c, n-1)
        self.move(nums, 0, c-1)
        self.move(nums, 0, n-1)

        return nums
he = Solution()

print(he.segregateElements(nums))


class Solution:
    def move(self, nums,low,high) :
        while low < high :
            nums[low], nums[high] = nums[high], nums[low]
            low+=1
            high-=1
    def rotateArr(self, nums, d):
        # code here
        n = len(nums)    
        self.move(nums,d,n-1)
        self.move(nums,0,d-1)
        self.move(nums,0,n-1)
        return nums
nums = [1,2,3,4,5]
d = 2 
w = Solution()
print(w.rotateArr(nums,d))


class Solution:
    def transpose(self, nums):
        # code here
        r = len(nums)
        c = len(nums[0])

        for i in range(r):
            for j in range(i+1,c):
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
        return nums

def thee(nums) :
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        if i != 0 and nums[i] == nums[i-1] :
            continue

        j = i+1
        k = n-1
        while j < k :
            tot = nums[i]+nums[j]+nums[k]
            if tot == 0 :
                res.append(nums[i],nums[j],nums[k])
                j+=1
                k-=1

                while j < k and nums[j] == nums[j-1]:
                    j+=1
                while j < k and nums[k] == nums[k+1] :
                    k-=1


            elif tot <  0 :
                j+=1
            else :
                k-=1
    return res 

def comvert2deci(x:str) -> int :
    decimal = 0
    index = len(x)-1
    power = 0 
    while index >= 0:
        num = int(x[index]) * (2**power)
        decimal+=num
        power+=1
        index-=1
    return decimal
nums = [0,1,2,3,4,5]
print(nums[0])
print(nums[1])
print(nums[2])


nums = [4,5,0,1,9,0,5,0]
def movepacket(nums) :
    n = len(nums)
    start = 0
    for i in range(n):
        if nums[i] != 0 :
            nums[start], nums[i] = nums[i], nums[start]
            start+=1
movepacket(nums)
print(nums)

nums = [1,0,2,0,1,0,2]
def movepacket(nums) :
    n = len(nums)
    start = 0
    for i in range(n):
        if nums[i] == 0 :
            nums[start], nums[i] = nums[i], nums[start]
            start+=1
movepacket(nums)
print(nums)

def hehe(nums) :
    n = len(nums)
    my_set = set()
    long = 0 
    for i in range(n):
        my_set.add(nums[i])
    for num in my_set :
        if num-1 not in my_set :
            x = num
            count = 1 
            while x+1 in my_set :
                count+=1
                x= x+1
            long = max(long,count)
    return long 

nums = [7,4,8,2,9]
print(hehe(nums))


def piro(nums) :
    res = 1
    ld = 0
    while nums > 0 :
        ld = nums % 10 
        res = res * ld
        nums = nums // 10 
    return res
print(piro(5244))

def calfine(nums, f, d) :
    n = len(nums)
    c = 0
    ans = 1
    if d % 2 == 0 : # so the fine will be collected from odd vehicles
        for i in range(n) :
            if nums[i] % 2 != 0 :
                c+=1
        ans = c * f
    else :
        for i in range(n) :
            if nums[i] % 2 == 0 :
                c+=1
        ans = c * f
    return ans
print(calfine([5,2,3,7], 200, 12))
print(calfine([2,5,1,6,8], 300, 3))

# have to fo questions that involve the logic of permutation 
