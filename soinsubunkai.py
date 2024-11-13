def soinsuRist(n):
    n2 = int(n/2)
    r = []
    for i in range(1,n2+1):
        c = 0
        for j in range(1,n2+1):
            if i % j == 0:
                c += 1
        if c == 2:
            r.append(i)
    r.append(n)
    return r

def insuRist(a):
    b = 0
    c = soinsuRist(a)
    d = []
    while a!= 1:
        if(a % c[b]) == 0:
            a = a // c[b]
            d.append(c[b])
        else:
            b = b + 1     
    return d

def bekijyoRist(a):
    r = []
    c = 1
    for i in range(1, len(a)):
        if a[i-1] == a[i]:
            c += 1
        else:
             r.append(c)
             c = 1
    r.append(c)
    return r

def createSiki(a,b):
    s = ""
    c = 0
    c2 = 0
    while c < len(a):
        if b[c2] == 1:
            s += str(a[c]) + " × "
        else:
            s += str(a[c]) + "^" + str(b[c2]) + " × "
        
        c += b[c2]
        c2 += 1
        
    s = s[:-3]
    return s

n = int(input())
a = insuRist(n)
b = bekijyoRist(a)
print(createSiki(a,b))