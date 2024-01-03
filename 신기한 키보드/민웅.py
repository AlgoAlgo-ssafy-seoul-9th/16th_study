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