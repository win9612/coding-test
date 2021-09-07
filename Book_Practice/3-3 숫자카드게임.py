# arr[n][m]

n, m = map(int, input().split())

arr = []
tmp = [0 for i in range(m)]

i = 0
while i < n : 
    tmp = list(map(int, input().split()))
    if len(tmp) != m :
        print("{0}개의 숫자를 입력하세요.".format(m))
    else : 
        arr.append(tmp)
        i += 1
    
tmp = [0 for i in range(n)]
for i in range(n) :
    tmp[i] = min(arr[i])

result = max(tmp)
print(result)