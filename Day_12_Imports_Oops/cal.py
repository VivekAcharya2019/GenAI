def add(a, b):
    return a+b

def Subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        return "Can not divide"
    return a/b

print(__name__)
if __name__ == "__main__":
    x = 23
    y = 47

    res = add(x, y)
    print(res)