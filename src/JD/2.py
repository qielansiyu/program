n = int(input())
str = list(input())
count = 1
pre = str[0].islower()
for i in range(1,len(str)):
    if str[i].islower():
        flag =1
    else:
        flag =0
    if flag == pre:
        count+=1
    else:count+=2
    pre = flag
print(count)
