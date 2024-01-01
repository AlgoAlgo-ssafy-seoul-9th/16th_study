# 1780 종이의 개수
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 1/3칸 돌리기
def devide(start_x:int, end_x:int, start_y:int, end_y:int) -> None:
    global answer
    # 1칸만 남았을 때
    if end_y - start_y <= 1:
        answer[field[start_y][start_x]] += 1
        return
    # 칸 내에 모두 같은 수 일때
    if conquer(start_x, end_x, start_y, end_y):
        answer[field[start_y][start_x]] += 1
        return
    # 중간지점 찾기
    x1_3, x2_3 = start_x+(end_x-start_x)//3, start_x+(end_x-start_x)//3*2
    y1_3, y2_3 = start_y+(end_y-start_y)//3, start_y+(end_y-start_y)//3*2
    
    # 재귀
    for sy, ey in [(start_y,y1_3),(y1_3,y2_3), (y2_3,end_y)]:
        for sx, ex in [(start_x,x1_3),(x1_3,x2_3), (x2_3,end_x)]:
            devide(sx, ex, sy, ey)

    return

# 모두 같은 수 인지 탐색
def conquer(start_x:int, end_x:int, start_y:int, end_y:int) -> int:
    tmp = field[start_y][start_x]
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            if field[y][x] != tmp:
                return 0
            tmp = field[y][x]
    return 1


if __name__ == "__main__":
    N = int(input().strip())
    field = [list(map(int, input().split())) for _ in range(N)]
    answer = defaultdict(int)
    devide(0,N,0,N)
    for i in range(-1, 2):
        print(answer[i])