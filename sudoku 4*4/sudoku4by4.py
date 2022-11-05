import random

body = (1,2,3,4)

def pg(olis,tem,cha,bha):
    if olis==a:
        ap=[]
        pc=[]
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
                    olis[x]=random.choice(cha)
                    ap.append(y)
                    pass
    if olis==b:
        ap=[]
        pc=[]
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
                    olis[x]=random.choice(cha)
                    ap.append(y)
                    pass           
    if olis==c:
        ap=[]
        pc=[]
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
                    olis[x]=random.choice(cha)
                    ap.append(y)
                    pass
    if olis==d:
        ap=[]
        pc=[]
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
                    olis[x]=random.choice(cha)
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

    #print(olis,"place vacant=tem",tem,"jo  number line me  posssible ha=cha",cha,"jo number pahale se ha=bha",bha)
    return pg(olis,tem,cha,bha) 
            

while True:
    #global a,b,c,d
    a1 = [1,0,0,0]
    b1 = [0,2,0,0]
    c1 = [0,1,3,2]
    d1 = [2,3,1,4]
    a=a1
    b=b1
    c=c1
    d=d1
    bz=[]
    if 0 in a or b or c or d:
        for mno in range(4):
            if 0 in a:
                a=new(a)
            if 0 in b:
                b=new(b)
            if 0 in c:
                c=new(c)
            if 0 in d:
                d=new(d)
            e=a+b+c+d
            if 0 not in e:
                break
            else :
                pass
        pass
    e=a+b+c+d
    if 0 not in e:
        break
print(a,b,c,d,sep="\n")
