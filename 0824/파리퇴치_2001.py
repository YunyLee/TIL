import sys
sys.stdin = open('input_2001.txt', 'r')

# 파리퇴치

TC = int(input())

for test_case in range(1, TC+1):
    N, M = map(int,input().split())
    FLY_LIST = [list(map(int,input().split())) for _ in range(N)]
    flies_sum = 0

    # 큰 정사각형 : 0 ~ N - M
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 작은 정사각형 : 0 ~ M - 1
            compare_sum = 0
            for k in range(M):
                for m in range(M):
                    compare_sum += FLY_LIST[i+k][j+m]
            if flies_sum < compare_sum:
                flies_sum = compare_sum

    print('#{} {}'.format(test_case, flies_sum))