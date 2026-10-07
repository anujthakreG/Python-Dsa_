# top 50 question :- 

#1 >  check even or odd :-
"""n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")"""

#2 > prime number -> dont know

#3 > factorial of a number :
def fact(n) :
    if n == 1 or n == 0 :
        return n 
    return n * fact(n-1)
print(fact(5))

# 4 > Fibonacci Series (First N Terms)

def fib(n) :
    if n == 0 or n == 1 :
        return n 
    return fib(n-1) + fib(n-2)

# n = int(input("Enter number of terms: "))   # the user input
n = 5
for i in range(n):
    print(fib(i), end=" ")


# 5 > reverse a number 
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


arr = [2,3,4,6,8,9]
t = 10 
def ts(nums,target) :
    t = target
    n = len(nums)
    freq = {}
    for i in range(n):
        rem = t - nums[i]
        if rem in freq :
            return (freq[rem],i )
        else :
            freq[nums[i]] = i
print(ts(arr,10))


def fac(n):
    if n == 0:
        return 1

    return n * fac(n-1)
print(fac(5))


# n = 3 
n = int(input("enter the number :- "))
brackets = [""] * (n*2)
res = []

def func(index,total,brackets, res) :
    if index >= len(brackets) :
        if total == 0 :
            res.append("".join(brackets))
        return 
    if total > (n*2) // 2 :
        return 
    elif total < 0 :
        return 
    brackets[index] = "("
    Sum = total+1
    func(index+1,Sum,brackets,res)
    brackets[index] = ")"
    Sum = total - 1
    func(index+1,Sum,brackets, res)

func(0,0,brackets,res)
print(res)

