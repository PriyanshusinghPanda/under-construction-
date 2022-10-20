body = (1,2,3,4)
global a,b,c,d
a = [1,4,0,0]
b = [0,2,0,0]
c = [4,1,3,2]
d = [2,3,1,4]

def pg(olis,tem,cha,bha):
    if olis==a:
        ap=[]
        for x in tem:
            temp=[]
            if b[x]!=0:
                temp.append(b[x])
            if c[x]!=0:
                temp.append(c[x])
            if d[x]!=0:
                temp.append(d[x])
            for az in ap:
                if az not in temp:
                    temp.append(az)
            for z in bha:
                if z not in temp:
                    temp.append(z)

            for y in cha:
                if y not in temp:
                    a[x]=y
                    ap.append(y)
                    pass
    if olis==b:
        ap=[]
        for x in tem:
            temp=[]
            if a[x]!=0:
                temp.append(a[x])
            if c[x]!=0:
                temp.append(c[x])
            if d[x]!=0:
                temp.append(d[x])
            for az in ap:
                if az not in temp:
                    temp.append(az)
            for z in bha:
                if z not in temp:
                    temp.append(z)
            
            for y in cha:
                if y not in temp:
                    b[x]=y
                    ap.append(y)
                    pass           
    if olis==c:
        ap=[]
        for x in tem:
            temp=[]
            if a[x]!=0:
                temp.append(a[x])
            if b[x]!=0:
                temp.append(b[x])
            if d[x]!=0:
                temp.append(d[x])
            for az in ap:
                if az not in temp:
                    temp.append(az)
            for z in bha:
                if z not in temp:
                    temp.append(z)
            
            for y in cha:
                if y not in temp:
                    b[x]=y
                    ap.append(y)
                    pass
    if olis==d:
        ap=[]
        for x in tem:
            temp=[]
            if a[x]!=0:
                temp.append(a[x])
            if c[x]!=0:
                temp.append(c[x])
            if b[x]!=0:
                temp.append(b[x])
            for az in ap:
                if az not in temp:
                    temp.append(az)
            for z in bha:
                if z not in temp:
                    temp.append(z)
            
            for y in cha:
                if y not in temp:
                    d[x]=y
                    ap.append(y)
                    pass
    return olis


def new(olis):
    tem = [] # place valcant
    cha = [] # jo  number line me  posssible ha
    bha = [] # jo number pahale se ha
    for x in range(len(olis)):
        if olis[x] in body:
            bha.append(olis[x])
        else:
            tem.append(x)
    for x in body:
        if x not in olis:
            cha.append(x)
    return pg(olis,tem,cha,bha) 
            

while 0 in a or b or c or d:
    if 0 in a:
        a=new(a)
    if 0 in b:
        b=new(b)
    if 0 in c:
        c=new(c)
    if 0 in d:
        d=new(d)
    break
print(a,b,c,d,sep="\n")
