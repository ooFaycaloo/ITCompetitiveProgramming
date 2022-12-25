t=[]
t=input("inserez votre list")
x=input("valeur chercher")

def find_element(t,x):
    for i in t:
       
        if (i==x):
        
            return 1
        
    return 0

print(find_element(t,x))