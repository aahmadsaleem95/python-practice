username = "chaiaurcode"

def func():
    # username = "chai"
    print(username)

print(username)
func()

x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 88

# func3()
# print(x)

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()
#factory function and closures are same
def chaicoder(num):
    def actual(x):
        return x**num
    return actual
print(chaicoder)
f = chaicoder(2)
print(f)
g = chaicoder(3)

print(f(3))
print(g(3))