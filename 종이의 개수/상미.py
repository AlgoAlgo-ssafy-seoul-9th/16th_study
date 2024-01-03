## 백준 1780 _ 종이의 개수

import sys
input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

answer = {-1:0, 0:0, 1:0}       # 개수 저장할 딕셔너리

def samenumber(x, y, n):
    if n == 1: 
        answer[nums[x][y]] += 1
        return
    
    tmp = nums[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # tmp와 다른 숫자가 발견되면
            if nums[i][j] != tmp:
                n //= 3 
                samenumber(x, y, n) # 1행
                samenumber(x, y+n, n)
                samenumber(x, y+2*n, n)
                
                samenumber(x+n, y, n) # 2행
                samenumber(x+n, y+n, n)
                samenumber(x+n, y+2*n, n)
                
                samenumber(x+2*n, y, n) # 3행
                samenumber(x+2*n, y+n, n)
                samenumber(x+2*n, y+2*n, n)
                return  #### 쪼갰으면 기존의 탐색은 종료 ####

    # 사각형 전부 기준과 같은 숫자인 경우 카운트
    answer[tmp] += 1
    return

samenumber(0, 0, N)

for i in range(-1, 2): 
    print(answer[i])