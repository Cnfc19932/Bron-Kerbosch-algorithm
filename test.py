import itertools
def MatrixMade(n):
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in range(n):
            if (i==j):
                matrix[i]+=[(0)];
            else: matrix[i]+=[(-999999999)]
    return matrix

def new_set(old_set,v,m):
    new_set1=set()
    for i in old_set:
        if m[i-1][v-1]>-1:  new_set1.add(i)
    return new_set1
def prov(not1,candidates1,m1):
    for i in not1:
        k=1
        for j in candidates1:
            if (m1[i-1][j-1]<0):
                k=0
                break
        if k==1:
            return (False)
    return (True)
compsub=set()
klik=[()]
max_k=0
on=0
def extended(candidates3,not3,m1):
    global compsub,klik,max_k,on
    print(list(not3)," ",on," ",list(candidates3))
    while(not(len(candidates3)==0)and(prov(not3,candidates3,m1))):
        v=list(candidates3)[0]
        print(list(not3)," ",on," ",list(candidates3))
        candidates3.pop()
        compsub.add(v)
        new_candidates=new_set(candidates3,v,m1)
        new_not=new_set(not3,v,m1)
        on=on+1
        if (len(new_candidates)==0)and (len(new_not)==0):
            if len(compsub)>1:
        #       print ("Размер ",len(compsub)," Вершины: ",compsub)
                klik+=[(list(compsub))]
                if len(compsub)>max_k:max_k=len(compsub)
        else: extended(new_candidates,new_not,m1)
        not3.add(v)
        compsub.discard(v)
        candidates3.discard(v)
n=int(input("Число вершин: "))
M=MatrixMade(n)
k=int(input("Число граней: "))
print("Введите ",k," строк вида x y(где x,y вершины ребер графа): ")
for i in range(k):
    o,s=map(int,input('').split())
    if not(o==s):
        M[o-1][s-1]=1;
        M[s-1][o-1]=1;
candidates=set(i for i in range(1,n+1))
not0=set()
extended(candidates,not0,M)
#print (klik[1:])

for j in range(2,max_k+1):
    print ("Клики размером ",j,": ")
    for i in klik[1:]:
        if len(i)>j-1:
            print(list(itertools.combinations(i,j)))
print(on)




