'''某学术会议上，一共有n个人参加，现在已知每个人会的语言（一个人可能不会任何语言）。现在有一种学习机，每一个学习机可以在会议期间使一个人暂时掌握一种自己不会的语言，
问要使得任意两人都要能直接或者间接的交流至少准备多少个学习机？

间接交流的意思是：可以通过其他参加会议的人翻译（可能或出现很多人一起帮忙翻译的情况）进行交流。如：第一个人和第二个人会第一种语言，第二个人和第三个人会第二种语言，
那么第一个人可以和第三个人进行交流（通过第二个人的翻译）
第一行3个数n,m,k代表人数，语言数，已知的信息数 接下来k行，每行两个数u,v，代表第u个人会第v种语言
输出需要准备的学习机的个数
3 3 2
2 3
3 1

2
'''
#依据人会的语言和会语言的人构成联通域连通域外的+1
n,m,k = list(map(int,input().split()))
peo = [[] for i in range(n+1)]
lan = [[] for i in range(m+1)]
for i in range(k):
    tmp = list(map(int, input().strip().split()))
    peo[tmp[0]].append(tmp[1])
    lan[tmp[1]].append(tmp[0])
flag = [0 for i in range(n+1)]
res = 0
print(flag)
for i in range(1, n+1):
    if flag[i] == 0:
        res += 1
        q = [i]
        flag[i] = 1
        while(len(q)!=0):
            cur = q.pop()
            for a in range(len(peo[cur])):
                for j in range(len(lan[peo[cur][a]])):
                    if flag[lan[peo[cur][a]][j]] == 0:
                        q.append(lan[peo[cur][a]][j])
                        flag[lan[peo[cur][a]][j]] = 1

if k == 0:
    print(res)
else:
    print(res-1)