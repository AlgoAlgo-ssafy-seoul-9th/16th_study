## 벡준 _1796_신기한 키보드

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
