n, m = input().split()
n = int(n)
m = int(m)
n_li = []
m_li = []
for i in range(n):
    temp = int(input())
    n_li.append(temp)
for i in range(m):
    temp = int(input())
    m_li.append(temp)

ans = [0]*n
np = 0
for i in range(m):
    #m_li[i]が0になるまで繰り返す
    while m_li[i] != 0:
        #もしm_li[i]がn_li[np]より小さかったら、そのままans[np]にm_li[i]を入れる。
        if m_li[i] < n_li[np]:
            ans[np] += m_li[i]
            m_li[i] = 0
            if np+1 == n:
                np = 0
            else:
                np += 1
        #もしm_li[i]がn_li[np]より大きかったら、ans[np]にn_li[np]を入れる。
        else:
            ans[np] += n_li[np]
            #m_li[i]はn_li[np]減る。
            m_li[i] -= n_li[np]
            if np+1 == n:
                np = 0
            else:
                np += 1

for i in ans:
    print(i)