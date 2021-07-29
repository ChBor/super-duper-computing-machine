#1
import random
l=[]
for i in range(0, 5):
    l.append(random.randint(1,5))
print(l)
t=tuple(l)
print(t)
print("\n")




#2
sl=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#sl=[(10, 20, 100), (40, 50, 100), (70, 80, 100)]
for i in sl:
    print ([i[:-1]+(100,)], end=" ")
print("\n")




#3
a=(1, 2, 3, 4); b=(3, 5, 2, 1); c=(2, 2, 3, 1)
#d=(6, 9, 8, 6)
result=0
result1=0
result2=0
result3=0
f=[]
for i in range(len(a)):
    result = a[0] + b[0] + c[0]
    result1 = a[1] + b[1] + c[1]
    result2 = a[2] + b[2] + c[2]
    result3 = a[3] + b[3] + c[3]
f.append(result)
f.append(result1)
f.append(result2)
f.append(result3)
d=tuple(f)
print(d)
print("\n")





#4
s=set()
for _ in range(0, 10):
    s.add(random.randint(1, 100))
print(s)
A=int(input("Enter value:"))
iF=False
for i in s:
    if i==A:
        iF=True
        break
print(iF)
print("\n")





#5
a=set()
b=set()
for i in range(0, 5):
    a.add(random.randint(1, 10))
    b.add(random.randint(1, 10))
print(a)
print(b)
c=set(a&b)
print("Общие элементы:", c)
print("\n")




#6
A=set()
B=set()
for i in range(0, 5):
    A.add(random.randint(1, 5))
    B.add(random.randint(1, 5))
print("A:", A)
print("B:", B)
C=A.difference(B)
print("C:", C)
print("\n")




#7
s1=set()
s2=set()
for i in range(0, 10):
    s1.add(random.randint(1, 100))
    s2.add(random.randint(1, 100))
print(s1)
print(s2)
s3=s1-s2
print(s3)



