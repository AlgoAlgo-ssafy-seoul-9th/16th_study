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