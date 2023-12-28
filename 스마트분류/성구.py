# 스마트분류
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