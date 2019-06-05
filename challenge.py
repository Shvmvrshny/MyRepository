a = input("enter 1st segment of an IP address")
aseg = ''
aIP = ''
a1=''
b1=''
c1=''
if len(a)<=3:
    for i in range(0, len(a)):
        if a[i] in '0123456789':
            aseg += a[i]
            a1=1
        else:
            break

else:
    print("invalid")
################################################
b=''
bseg = ''
bIP = ''

if a1==1:
    b = input("enter 2nd segment of an IP address")
    if len(b)<=3:
        for j in range(0,len(b)):
            if b[j] in '0123456789':
                bseg += b[j]
                b1=1
            else:
                break

    else:
        print("invalid")
else:
    print("invalid")
###############################################


c=''
cseg = ''
cIP = ''
if b1==1:
    c = input("enter 3rd segment of an IP address")
    if len(c)<=3:
        for k in range(0,len(c)):
            if b[k] in '0123456789':
                cseg += c[k]
                c1=1
            else:
                break

    else:
        print("invalid")
else:
    print("invalid")
###############################################

d=''
dseg = ''
dIP = ''
if c1==1:
    d = input("enter 4th segment of an IP address")
    if len(d)<=3:
        for l in range(0,len(d)):
            if b[l] in '0123456789':
                dseg += d[l]
                d1=1
            else:
                break

    else:
        print("invalid")
else:
    print("invalid")

##############################################

print("{}.{}.{}.{}".format(aseg,bseg,cseg,dseg))

