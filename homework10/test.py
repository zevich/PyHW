a =[1,3,5,6,9]
for i, p in enumerate(a):
    print(i,p)
    if p == 5:
        a.pop(i)
print (a)