a = [0 , 6 , 10 , 2 , 8]
b = [1 , 3 , 5 , 7]

a.sort()
b.sort()

print(a)
print(b)
min = a[0]
for i in range (len(b)) :
    for j in range (len(a)) : 
        if b[i]<a[j] :
            x=a[j]
            a[j]=b[i]
            b[i]=x

b.sort()

print(a)
print(b)
    
