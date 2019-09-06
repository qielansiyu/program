'''
8
0.1 0
0.15 0
0.2 1
0.5 0
0.6 0
0.75 1
0.9 1
0.9 1
'''
'''
n = int(input())
sample = {}
T = 0
F = 0
for i in range(n):
    m, _ = map(float, input().split())
    if m in sample:
        if _ == 1:
            T += 1
            sample[m][1]+=1
            sample[m][3]+=1

        elif _ == 0:
            F+=1
            sample[m][0]+=1
            sample[m][2]+=1
    else:
        if _ == 1:
            T+=1
            sample[m]=[0,1,F,T]
        else:
            F+=1
            sample[m]=[1,0,F,T]
ks = []
for k,v in sample.items():
    a = 0
    b = 0
    if v[2] == 0:
        a = 0
    else:
        a = v[2]/F
    if v[3] == 0:
        b = 0
    else:
        b = v[3]/T
    tmp = a-b if a-b>=0 else b-a
    ks.append(tmp)
print(round(max(ks),4))
'''
'''

'''
n = int(input())

num = []
l0 =0
l1 = 0
for i in range(n):
    s=input().split()
    num.append([float(s[0]),int(s[1])])
    if int(s[1])==0:
        l0+=1
    else:
        l1+=1
t0=0
t1=0
ks=0
for i in range(n):
    if num[i][1]==0:
        t0+=1/l0
    elif num[i][1]==1:
        t1+=1/l1
    ks=max(ks,t0-t1)
print(round(ks,4))
