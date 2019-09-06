#一元一次方程组
s = input()

r = eval(s.replace('=', '-(') + ')', {'X': 1j})
ans = 0
flag = True
try:
    ans = -r.real / r.imag
except:
    print('-1')
    flag = False

if flag:
    if ans % 1 == 0 and int(ans) > 0:
        print(int(ans))
    else:
        print('-1')