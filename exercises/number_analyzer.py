a = 45224

a = int(input())


def sum_(num):
    _sum = 0
    while num:
        _sum += num % 10
        num //= 10
    return _sum

print("sum:", sum_(a))

def product_(num):
    p = 1
    while num:
        p *=  num % 10
        num //= 10
    return p
            

print("product:", product_(a))

def reverse_(num):
    arr = list(str(num))
    for i in range(len(arr)// 2):
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
    return "".join(arr)
print("Reversed:", reverse_(a))



def palindrome_(num):
    arr = str(num)
    for i in range(len(arr)// 2):
        if arr[i] !=arr[len(arr) - i - 1]:
            return False
        
    return True

print("Is Palindorme:", palindrome_(a))

def find_largest_digit(num):
    max_ = 0
    while num:
        p = num % 10
        max_ = max(max_, p)
        num //= 10
    return max_

print("Largest Digit:", find_largest_digit(a))

def find_smallest_digit(num):
    min_ = float("inf")
    while num:
        p = num % 10
        min_ = min(min_, p)
        num //= 10
    return min_

print("Smallest Digit:", find_smallest_digit(a))

def fact_(num):
    if num <= 1:
        return 1
    return num * fact_(num - 1)

print("factorial:", fact_(4))

def count_even_odd(num):
    even_ = 0
    odd_ = 0
    while num:
        p = num % 10
        even_ += 1 if p % 2 == 0 else 0
        odd_ += 1 if p % 2  else 0
        num //= 10
    return even_, odd_

print("even count, odd count:", count_even_odd(a))

