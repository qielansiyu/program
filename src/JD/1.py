str = []
dic = {}
while 1:
    tmp = input()
    if tmp != '':
        tmp = list(tmp.split())
        str.append(tmp)
        if tmp[0] in dic:
            dic[tmp[0]] +=1
        else:
            dic[tmp[0]] = 1
    else:
        break
list1 = sorted(dic.items(),key=lambda x:x[1],reverse=True)
xing = []
tmp =[list1[0][0]]
for i in range(1,len(list1)):
    if list1[i][1] == list1[i-1][1]:
        tmp.append(list1[i][0])
    else:
        xing.append(tmp)
        tmp=[]
        tmp.append(list1[i][0])
xing.append(tmp)
for i in range(len(xing)):
    for j in range(len(str)):
        if str[j][0] in xing[i]:
            print(' '.join(str[j]))