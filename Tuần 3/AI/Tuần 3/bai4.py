import math
def cos(x,dem):
    cosx = 0
    a = 1
    n = 0
    while n<=dem:
        cosx +=a
        n+=1
        a = pow(-1,n)*pow(x,2*n)/math.factorial(2*n)
    return cosx
x= (2*math.pi)/3
cosx=cos(x,10)
print(cosx)
