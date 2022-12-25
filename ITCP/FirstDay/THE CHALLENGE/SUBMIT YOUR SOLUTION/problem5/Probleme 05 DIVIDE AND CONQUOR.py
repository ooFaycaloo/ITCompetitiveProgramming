import math
t=[[0,5],[7,4],[4,5],[1,53],[1,54],[4,4]]
minn =math.dist(t[0],t[1])
for i in t :
    for j in t:
        if i==j :
            continue
        x= math.dist(i,j)
        print(x)

        if (x>0):
            if (minn>x):
                i_min=i
                j_min=j
                minn=x

print(minn ,i_min,j_min)
    

