import sys
sys.stdin = open('input_1860.txt', 'r')

# swea 1860 문제

TC = int(input())

for test_case in range(1, TC+1):
    N, M, K = map(int, input().split()) #N명 M초 K개
    TIME = list(map(int,input().split()))
    # 손님이 들어오는 순서를 정렬하자.
    TIME.sort()#reverse=True하면 거꾸로 가능

    result = 'Possible'
    for i in range(N):
        tmp = (TIME[i] // M) * K # 아직 아무도 안 먹었다.
        if (tmp - 1 -i) < 0: # -1은 현재 손님꺼, i는 이전 손님들이 가져간 수
            result = 'Impossible'
            break
    print('#{} {}'.format(test_case, result))



    # result = ''
    #
    # if sum(TIME)//(M*N) <1:
    #     result = 'Impossible'
    # else:
    #     result = 'Possible'
    #
    # print('#{} {}'.format(test_case, result))
    #
    #
    # # 식 세울때
    #
    # ( 2초일때때 // 2초마다 )  1개씩

