"""

def fn():
    print("hello")
fn()

def fn(a):
    print(a)
fn("hello world")

def add(a,b):
    c=a+b
    print(c)

add(b=2,a=3)


def add(a,b=3):
    d=a*a
    c=b*b*b
    print(c,d)

add(a=2)

def add(a=3,b=2)
    d=a*a
    c=b*b
a,b=add(2,3)
print(str(d))+" "+str(c))

n=6
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if (sum==n):
        return True
    else:
        return False
print(perfect(6))


n=6
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if (sum==n):
        return True
    else:
        return False
for i in range(1,1001):
    if(perfect(i))==True:
        print(i)
"""
n=int(input("enter any number"))
def feb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return feb(n-1)+feb(n-2)
print(feb(n))

