import sys
sys.stdin = open('input_1220.txt', 'r')

def solve(arr, N):
    cnt = 0

    for c in range(N):
        flag = 0    # N극을 못 찾음
        for r in range(N):
            if flag == 0 and arr[r][c] == 1: # N극을 찾음
                flag = 1     #N극 찾음
            elif flag == 1 and arr[r][c] == 2 : # S극을 찾음
                cnt += 1
                flag = 0

    return cnt

TC = 10
for test_case in range(1, TC+1):
    N = int(input())  # 2차원 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(test_case, solve(arr, N)))