def add(a,b):
    return a+b 

def subtract(a,b):
    return a-b 

def multiply(a,b):
    return a*b 

def divide(a,b):
    if b == 0 :
        return "Can not devide"
    return a/b 

# print("This is outside if main condition")

# below part will run only if i directly run this file
if __name__ == "__main__":
    x = 12 
    y = 10
    output = add(x,y)
    print("Addition Results", output)
