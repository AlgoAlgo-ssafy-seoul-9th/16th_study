# 1796 신기한 키보드
import sys
input = sys.stdin.readline


def dfs(idx:int, word_idx:list, word:dict, cnt:int, now_index:int) -> None:
    global answer, S
    if idx == len(word_idx):
        answer = min(answer, cnt + len(S))
        return
    word_lift = (word[word_idx[idx-1]][1]-word[word_idx[idx-1]][0])
    dfs(idx+1, word_idx, word, cnt+abs(now_index - word[word_idx[idx]][1]) + word_lift, word[word_idx[idx]][1])
    dfs(idx+1, word_idx, word, cnt+abs(now_index - word[word_idx[idx]][0]) + word_lift, word[word_idx[idx]][0])

    return


def solution(S:str) -> None:
    global answer
    word = {}
    for i in range(len(S)):
        if S[i] not in word.keys():
            word[S[i]] = [i, i]
        else:
            word[S[i]][1] = i

    word_idx = sorted(word.keys())
    if len(word_idx) == 1:
        answer = len(S) + (word[word_idx[0]][1]-word[word_idx[0]][0])
    else:
        dfs(1, word_idx, word, (word[word_idx[0]][1]-word[word_idx[0]][0]), word[word_idx[0]][1])
    return


if __name__ == "__main__":
    S = input().strip()
    answer = 25001
    solution(S)
    print(answer)