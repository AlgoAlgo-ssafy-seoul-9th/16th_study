# 16th_study

16주차 스터디

# 스터디 사전 문제

[바로가기](https://www.acmicpc.net/problem/1780)

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [종이의 개수](https://www.acmicpc.net/problem/1780)

### [민웅](./종이의%20개수/민웅.py)

```py
# 1780_종이의개수_number-of-papers
import sys
input = sys.stdin.readline

def papercheck(n, i_idx, j_idx):
    global answer
    tmp = paper[i_idx][j_idx]

    check = True
    for i in range(i_idx, i_idx+n):
        for j in range(j_idx, j_idx+n):
            if paper[i][j] == tmp:
                continue
            else:
                papercheck(n // 3, i_idx, j_idx)
                papercheck(n // 3, i_idx, j_idx + n // 3)
                papercheck(n // 3, i_idx, j_idx + 2*(n // 3))
                papercheck(n // 3, i_idx + n // 3, j_idx)
                papercheck(n // 3, i_idx + n // 3, j_idx + n // 3)
                papercheck(n // 3, i_idx + n // 3, j_idx + 2 * (n // 3))
                papercheck(n // 3, i_idx + 2*(n // 3), j_idx)
                papercheck(n // 3, i_idx + 2*(n // 3), j_idx + n // 3)
                papercheck(n // 3, i_idx + 2*(n // 3), j_idx + 2 * (n // 3))
                check = False
                break
        if check:
            continue
        else:
            break
    else:
        if tmp == -1:
            answer[0] += 1
        elif tmp == 0:
            answer[1] += 1
        else:
            answer[2] += 1

N = int(input().strip())
paper = [list(map(int, input().split())) for _ in range(N)]

answer = [0, 0, 0]

papercheck(N, 0, 0)
print(answer[0])
print(answer[1])
print(answer[2])

```

### [상미](./종이의%20개수/상미.py)

```py
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
```

### [병국](./종이의%20개수/병국.py)

```py
# 나누고 > 체크하는 과정 반복
# 일단 나눠
#  어떻게 체크할래 ? 합이 무조건 홀수다, 음수 홀수,
def cut(x,y,n):
    global minus,plus,zero
    check_num = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            # 다르면 9개로 자르자
            if arr[i][j] != check_num:
                for a in range(3):
                    for b in range(3):
                        cut(x+a*(n//3), y+b*(n//3), n//3)
                return
    if check_num == -1:
        minus+=1
    elif check_num == 1:
        plus+=1
    else:
        zero+=1
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
minus = 0
plus = 0
zero = 0
cut(0,0,n)
print(minus)
print(zero)
print(plus)
```

### [성구](./종이의%20개수/성구.py)

```py
# 1780 종이의 개수
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1/3칸 돌리기
def devide(start_x:int, end_x:int, start_y:int, end_y:int) -> None:
    global answer
    # 1칸만 남았을 때
    if end_y - start_y <= 1:
        answer[field[start_y][start_x]] += 1
        return
    # 칸 내에 모두 같은 수 일때
    if conquer(start_x, end_x, start_y, end_y):
        answer[field[start_y][start_x]] += 1
        return
    # 중간지점 찾기
    x1_3, x2_3 = start_x+(end_x-start_x)//3, start_x+(end_x-start_x)//3*2
    y1_3, y2_3 = start_y+(end_y-start_y)//3, start_y+(end_y-start_y)//3*2

    # 재귀
    for sy, ey in [(start_y,y1_3),(y1_3,y2_3), (y2_3,end_y)]:
        for sx, ex in [(start_x,x1_3),(x1_3,x2_3), (x2_3,end_x)]:
            devide(sx, ex, sy, ey)

    return

# 모두 같은 수 인지 탐색
def conquer(start_x:int, end_x:int, start_y:int, end_y:int) -> int:
    tmp = field[start_y][start_x]
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if field[y][x] != tmp:
                return 0
            tmp = field[y][x]
    return 1


if __name__ == "__main__":
    N = int(input().strip())
    field = [list(map(int, input().split())) for _ in range(N)]
    answer = defaultdict(int)
    devide(0,N,0,N)
    for i in range(-1, 2):
        print(answer[i])
```

</div>
</details>

<br/><br/><br/>

# 알고리즘

<details open>
<summary>접기/펼치기</summary>
<div markdown="1">

## 분할정복

[![분할정복](./사진파일/dividenconquer.png)](https://namu.wiki/w/%EB%B6%84%ED%95%A0%20%EC%A0%95%EB%B3%B5%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

### 설계

1. Divide
   - 문제가 분할이 가능한 경우, N개의 문제로 나누기
2. Conquer
   - 분할한 문제를 해결
3. Combine
   - 해결한 문제를 통합하여 본 문제를 해결

### 대표 알고리즘

1. [피보나치 수열](https://www.acmicpc.net/problem/10870)
2. 병합정렬(Merge sort)
   - [4 5 1 3 2]
3. 퀵정렬(Quick sort)

</div>
</details>

<br/><br/><br/>

# 지난 스터디 문제

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [스마트 물류](https://softeer.ai/practice/6279)

### [민웅](./스마트분류/민웅.py)

```py
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

HP = list(input().strip())
picked = [0]*N
cnt = 0

for i in range(N):
  if HP[i] == "P":
    # tmp = K
    # while True:
    #   if tmp == 0:
    #     break
    #   if i - tmp >=0:
    #     if HP[i-tmp] == "H" and not picked[i-tmp]:
    #       picked[i-tmp] = 1
    #       cnt += 1
    #       break
    #   if i + tmp <= N-1:
    #     if HP[i+tmp] == "H" and not picked[i+tmp]:
    #       picked[i+tmp] = 1
    #       cnt += 1
    #       break
    #   tmp -= 1
    for j in range(max(0, i-K), min(i+K+1, N)):
      if j != i:
        if HP[j] == "H" and not picked[j]:
          picked[j] = 1
          cnt += 1
          break

print(cnt)


```

### [상미](./스마트분류/상미.py)

```py

```

### [병국](./스마트분류/병국.py)

```py
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
```

### [성구](./스마트분류/성구.py)

```py
import sys
input = sys.stdin.readline

# P: 로봇, H:부품
def solution(N:int, K:int, conv:str) -> int:
  visited = [0] * N
  cnt = 0
  for i in range(N):
    if conv[i] == "H":
      for j in range(max(0, i-K), min(i+K+1, N)):
        if conv[j] == "P" and not visited[j]:
          visited[j] = 1
          cnt += 1
          break
  return cnt


if __name__ == "__main__":
  N, K = map(int, input().split())
  conv = input().strip()
  print(solution(N, K, conv))
```

## [신기한 키보드](https://www.acmicpc.net/problem/1796)

### [민웅](./신기한%20키보드/민웅.py)

```py
# 1796_신기한 키보드
import sys
input = sys.stdin.readline

def bt(score, idx, alpha):
    global ans
    if alpha == 26:
        if score < ans:
            ans = score
        return

    if score >= ans:
        return

    if s_lst[alpha]:
        min_lo = min(s_lst[alpha])
        max_lo = max(s_lst[alpha])
        if min_lo != max_lo:
            enter = len(s_lst[alpha])
            tmp1 = score + enter + abs(max_lo-idx) + (max_lo-min_lo)
            tmp2 = score + enter + abs(min_lo-idx) + (max_lo-min_lo)
            bt(tmp1, min_lo, alpha+1)
            bt(tmp2, max_lo, alpha+1)
        else:
            score += (abs(idx-min_lo)+1)
            bt(score, min_lo, alpha+1)
    else:
        bt(score, idx, alpha+1)


S = list(input().strip())

s_lst = [[] for _ in range(26)]
idx = 0

for s in S:
    s_lst[ord(s)-97].append(idx)
    idx += 1

ans = float('inf')

bt(0, 0, 0)
print(ans)

```

### [상미](./신기한%20키보드/상미.py)

```py
## 벡준 _1796_신기한 키보드
## 틀림
alp = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z': 26}
word = input().strip()
index = []
for w in word:
    index.append(alp[w])
# dp = [0] * len(word)
cnt = 0

def keyboard(tmp):
    global cnt
    minIdx = []
    if index == [27] * len(word):
        return cnt
    else:
        m = min(index)
        for i in range(len(word)):
            if m == index[i]:
                minIdx.append(i)
                index[i] = 27
        for idx in minIdx:
            cnt += abs(tmp-idx)
            tmp = idx
            keyboard(idx)
        return cnt

print(keyboard(0)+len(word))

```

### [병국](./신기한%20키보드/병국.py)

```py

```

### [성구](./신기한%20키보드/성구.py)

```py

```

</div>
</details>
