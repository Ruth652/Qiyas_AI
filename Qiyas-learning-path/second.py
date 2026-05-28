# *args and **kwargs are used in function definitions to allow for variable-length arguments.
def myFunc(*args , **kwargs):
    print("Non-keyword arguments:( * args)")

    for args in args:
        print(args)

    print("Keyword arguments:( ** kwargs)")
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    
myFunc("hey", "Welcome", first="python", mid='for', last='python')



def f1():
    s = "I love python"
    def f2():
        print(s)
    f2()
f1()


# anonymous function
def c1(x) : return x * x * x
c2 = lambda x: x * x * x
print(c1(7))
print(c2(7))



def ress(num):
    if num % 2:
        return num ** 3
    else:
        return num ** 2
print(ress(2))

# pass by refrence and pass by value 
# mutable - list, dict, set
# inmutable - int, float, string, tuple ( immutable objects cannot be changed after they are created, while mutable objects can be modified after they are created.)

def fact(num):
    if num == 0:
        return 1
    return num * fact(num -1)
print(fact(3))

def add_(num):
    if num == 0:
        return 0
    return num + add_(num -1)
print(add_(3))


def arr(num):
    num[0] = 10

a = [1, 2, 3, 4, 5]
arr(a)
print(a)


# list comprehensions

data = [1,2,3,4,5]
result = [value ** 2 + value / 2 for value in data]
print(result)

data2 = range(0, 15)
result2 = [value ** 3 if value % 2 else value ** 2 for value in data2]
print(result2)


# nested loop using list comprehensions
# making a 3x3 matric using it

# c = [[x,y, j] for x in range(3) for y in range(3) for j in range(3)]
# print(c)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [val for row in mat for val in row]
print(res)



# using lambda function with list comprehension

func = [lambda args=x:args * 10 for x in range(1, 5)]
for f in func:
    print(f())

# filtering using lambda function
c = [1, 2, 3, 4, 5]
filtered = list(filter(lambda x: x % 2 ==0 , c))
print(filtered)