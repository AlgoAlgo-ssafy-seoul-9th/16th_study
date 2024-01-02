# 2747 피보나치 수
import time
import sys
input = sys.stdin.readline

# dp : 1.91865 sec
def dp(n:int) -> int:
    if n == 0:
        return 0
    
    dp_list = [0] * (n+1)
    dp_list[1] = 1
    
    for i in range(2, n+1):
        dp_list[i] = dp_list[i-1] + dp_list[i-2]

    return dp_list[-1]

# 재귀 : 126.57475 sec
def fib(n:int) -> int:
    # n = 0, 1인경우 체크
    if n == 0:
        return 0
    if n == 1 or n==2:
        return 1
    # 이전 피보나치 수를 더하여 계산
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    # start = time.time()
    n = int(input())
    
    # print(fib(n))
    print(dp(n))
    # end = time.time()
    # print(f"시간 : {end-start:.5f} sec")