n,k = map(int,input().split())
arr = list(input())


where_robot = []
for i in range(len(arr)):
    if arr[i] == 'P':
        where_robot.append(i)
# p가 로봇, h가 부품
eat_list = [[] for _ in range(len(arr))]
for i in range(len(arr)):
    if arr[i] == 'P':
        for j in range(i-k,i+k+1):
            if j == i or j<0 or j>=len(arr) or j in where_robot:
                continue
            eat_list[i].append(j)
# print(eat_list)
# 로봇부터 시작하면 왼쪽을 계속 먹어들어가야한다

idx = 0
cnt = 0
v = [0] * (len(arr)+1)
while idx < len(arr):
    if arr[idx] == 'P':
        for product in eat_list[idx]:
            if v[product] == 0:
                v[product] = 1
                cnt += 1
                break
    idx += 1
print(cnt)