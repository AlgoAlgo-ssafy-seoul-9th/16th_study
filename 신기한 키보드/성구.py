# 1796 신기한 키보드
import sys
input = sys.stdin.readline

def solution(S:str) -> int:
    # settings
    words = {}      # 단어별 [첫 인덱스, 마지막 인덱스]
    for i in range(len(S)):
        if S[i] not in words.keys():
            words[S[i]] = [i,i]
        else:
            words[S[i]][1] = i
    word = sorted(words.keys())     # 정렬된 단어
    # print(word)
    # print(words)
    dp = [0,0]
    now_id = words[word[0]][1]
    dp[0] = words[word[0]][1]
    for now in range(1, len(word)):
        dist = words[word[now]][1] - words[word[now]][0]
        dp
            
    # print(dp)
    return min(dp) + len(S)


'''
def dfs(idx:int, word_idx:list, word:dict, cnt:int, now_index:int) -> None:
    global answer, S
    if idx == len(word_idx):
        answer = min(answer, cnt + len(S))
        return
    word_lift = (word[word_idx[idx]][1]-word[word_idx[idx]][0])
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
        dfs(1, word_idx, word, (word[word_idx[0]][1]), word[word_idx[0]][1])
    return


'''
if __name__ == "__main__":
    S = input().strip()
    
    print(solution(S))
    