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
```

### [병국](./종이의%20개수/병국.py)
```py
```

### [성구](./종이의%20개수/성구.py)
```py
```

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
```

### [상미](./신기한%20키보드/상미.py)
```py
```

### [병국](./신기한%20키보드/병국.py)
```py
```

### [성구](./신기한%20키보드/성구.py)
```py
```


</div>
</details>

