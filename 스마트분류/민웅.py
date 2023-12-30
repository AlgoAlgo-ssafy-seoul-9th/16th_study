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
          
      