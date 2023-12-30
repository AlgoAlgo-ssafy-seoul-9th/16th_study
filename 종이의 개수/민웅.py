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
