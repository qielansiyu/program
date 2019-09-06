st = list(input().split('='))

def f(s):
    t = [0,0]#t[0]存常数，t[1]存x前面的系数
    f = 1# f取符号，e取当前读到的数字
    flag_x= 0 #0无x，1有x
    flag_c=0
    tmp = 0

    tmp1 = []
    def aaa():
        nonlocal tmp1,flag_x,tmp,f,t,flag_c
        if len(tmp1) != 0:
            tmp = sum(tmp1)
            tmp1 = []
        flag_c = 0
        if flag_x == 0:
            t[0] += f * tmp
        else:
            if (tmp == 0):
                t[1] += f
            else:
                t[1] += f * tmp
            flag_x = 0
    #bb用于存放一个数
    for i in range(len(s)):
        if i == 0 and s[i]=='-':
            f=-1
        else:
            c = s[i]
            if c == '+':
                aaa()
                f=1
                tmp = 0
            elif c == '-':
                aaa()
                f=-1
                tmp=0
            elif c == '*':
                flag_c = 1
                if len(tmp1) != 0:
                    tmp = sum(tmp1)
                    tmp1=[]
            elif c=='X':
                flag_x = 1
            else:
                if flag_c== 0:
                    tmp = tmp*10+f*int(c)
                else:
                    tmp1 = tmp1*10
                    tmp1.append(int(c)*tmp)
    if len(tmp1)!=0:
        tmp = sum(tmp1)
    if flag_x ==1:
        if tmp ==0:
            t[1]+=f
        else:
            t[1] += tmp
    else:
        t[0] += tmp
    return t
if(len(st)!=2):
    print(-1)
else:
    a=0#l累计常数
    b=0#累计系数
    tmp = f(st[0])
    a += tmp[0]
    print(a)
    b += tmp[1]#// 等式右边
    print(b)
    tmp = f(st[1])
    a -= tmp[0]
    print(a)
    b -= tmp[1]
    print(b)
    if (a == 0 or b ==0 or (-a/b <=0)):
        print(-1)
    else:
        print(int(-a / b))#注意打印时候的符号