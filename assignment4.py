#tuple
#Question 1

l=(1,2,3, "a","b",[1,2,3])
print (len(l))

#Question 2
t=(12,11,10,14)
print(min(t))
print(max(t))


#Question 3
t=(2*3*5*6)
print(t)


#sets
#Question 1
a=input("enter the values")
b=input("enter the values")
c=input("enter the values")
d=input("enter the values")
e=input("enter the values")
s1=set([a,b,c])
s2=set([c,d,e])
#difference between two sets
s3=s1-s2
print(s3)
#comparison between two sets

print(s1>=s2)
print(s2<=s1)

#intersection of two sets
print(s1&s2)


#dictionary

#Question 1

name=input("enter any name")
marks=input("enter marks")
d={"name":name, "marks":marks}
print(d)


#Question 2

marks={"a":60,"b":68,"c":79, "d":98}
print (sorted(marks.values()))


#Question 3

l=["M","I","S","S","I","S","S","I","P","P","I"]
m=l.count("M")
i=l.count("I")
s=l.count("S")
p=l.count("P")
D={'m':m,'i':i,'s':s,'p':p}
print(D)