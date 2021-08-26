import sys
sys.stdin = open('input_1860.txt', 'r')

# swea 1860 문제

TC = int(input())

for test_case in range(1, TC+1):
    N, M, K = map(int, input().split()) #N명 M초 K개
    TIME = list(map(int,input().split()))
    result = ''

    if sum(TIME)//(M*N) <1:
        result = 'Impossible'
    else:
        result = 'Possible'

    print('#{} {}'.format(test_case, result))

