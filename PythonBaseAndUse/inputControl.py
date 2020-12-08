#a=input()
def sum2(a,b):
    if (not(isinstance(a,(int,float))) and not(isinstance(b,(int,float)))):
        return("all arguments are not a numbers")
    elif not((isinstance(a, (int, float)))):
        return("1st argument is not a number")
    elif not((isinstance(b, (int, float)))):
        return("2nd argument is not a number")
    else:
        return a+b

def sumT(a, b): #use type
    t = [int, float]
    if type(a) not in t and type(b) in t:
        return "1st argument is not a number"
    elif type(b) not in t and type(a) in t:
        return "2nd argument is not a number"
    elif type(a) not in t and type(b) not in t:
        return "all arguments are not a numbers"
    return a + b

def sum3(a,b):
    if (isinstance(a,(int,float))):
        if isinstance(b,(int,float)):
            return a + b
        else:
            return "2nd argument is not a number"
    elif isinstance(b,(int,float)):
        return "1st argument is not a number"
    else:
        return "all arguments are not a numbers"


a1="hj"
b1=56
print(sum3(a1,b1))

