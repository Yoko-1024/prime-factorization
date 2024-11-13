import math

def soinsuRist(n):#ルートn以下の素数のリスト作成
    n2 = int(math.sqrt(n))
    r = []
    for i in range(1,n2+1):
        c = 0
        for j in range(1,n2+1):
            if i % j == 0:
                c += 1
        if c == 2:
            r.append(i)
    return r

def sosuHantei(n):#nが素数ならばそのまま返し、素数でなければ割り切れる最小の素数を返す
    a=soinsuRist(n)
    b=len(a)
    c=0
    d=0
    while c < b:
        if n % a[c] == 0:
            d=a[c]
            break
        else:
            c += 1
    if b==c:
        d=n

    return d

def insuRist(n):#nの素因数リスト
    a = n
    r = []
    while a!= 1:
        b=sosuHantei(a)
        a = a // b
        r.append(b)
    return r

def bekijyoRist(a):#各素因数のべき数リスト
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

def createSiki(a,b):#素因数とべき数を合わせて素因数分解の式を生成
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
#print(soinsuRist(n))
a = insuRist(n)
#print(a)
b = bekijyoRist(a)
#print(b)
print(createSiki(a,b))