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

