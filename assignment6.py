#QUESTION 1
for i in range(10):
    a=int(input("enter any integer"))
    print(a)

#QUESTION 2
a=2
while(a==2):
     print("acadview")


#QUESTION 3
a=int(input("enter any number"))
b=int(input("enter any number"))
c=int(input("enter any number"))
d=int(input("enter any number"))
e=int(input("enter any number"))
l=[a,b,c,d,e]
l1=[]
for i in l:
    j=i**2
    l1.append(j)
print(l1)


#QUESTION 4
integers=[]
decimals=[]
strings=[]
list=["abc","123","345","8.0","xyz"]
for i in list:
    if i.isalpha():
        strings.append(i)
    elif i.isdigit():
        integers.append(int(i))
    else:
        decimals.append(float(i))
print(strings)
print(integers)
print(decimals)


#QUESTION 5
even=[]
odd=[]
for i in range(1,101):
    if (i%2==0):
        even.append(i)
    elif (i % 2 != 0):
        odd.append(i)

print("even is ",even)
print("odd is ",odd)


#QUESTION 6

for i in range(0,5):
    j=i+1
    print("*"*j)


#QUESTION 7
b={}
a=int(input("enter no of elements:"))
for i in range(a):
    key=input("enter key:")
    value=input("enter value:")
    b[key]=value
print(b)
for key in b:
    print(key)


#QUESTION 8
a=int(input("enter inputs"))
l=[]
for i in range(a):
    elements=input("enter elements:")
    l.append(elements)
c=input("enter elements to be search:")
for j in l:
    if j==c:
        l.remove(c)
        print(l)