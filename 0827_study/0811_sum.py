import sys
sys.stdin = open('input_1209.txt', 'r')

# 숙제 2일차 - sum

# 100개짜리는 디버깅 하기 힘드므로 예시에 나온 테스트 케이스로 진행해본다.
'''
0
4 4 3 2 1
2 2 1 6 5
3 5 4 6 7
4 2 5 9 7
8 1 9 5 6
'''

TC = 10
N = 100

def compare_max(max_num, sum_num):
    if sum_num > max_num:
        max_num = sum_num
    return max_num

# TC = 1
# N = 5

for test_case in range(1, TC+1):
    TC_NUM = int(input())
    T_LIST = [list(map(int,input().split()))  for _ in range(N)]

    max_num = 0 #가로 세로 대각선 양쪽 방향 모두 비교해서 가장큰 값을 담아줄 변수

    # 행의 합
    # 내가 더해야 하는 값
    # T_LIST[0][0] + T_LIST[0][1] + T_LIST[0][2] + T_LIST[0][3] + T_LIST[0][4]

    for i in range(N):
        sum_num = 0 # 행마다 합을 담아줄 변수
        for j in range(N):
            sum_num += T_LIST[i][j]
        max_num = compare_max(max_num, sum_num)
        # 값이 넘어간걸 비교해서 리턴을 했기 때문에, 변수에 저장을 해줘야 한다.
        # 리스트를 넘겼다면 리턴 안해도 원래 리스트에 영향을 미친다.
        # 값은 영향을 안 미친다. 따로 변수에 저장해줘야한다.

    # 열의 합
    for i in range(N):
        sum_num = 0 # 열마다 합을 담아줄 변수
        for j in range(N):
            sum_num += T_LIST[j][i]
        max_num = compare_max(max_num, sum_num)

    # \ 이쪽방향 대각선
    diagonal_sum = 0
    for i in range(N):
        diagonal_sum += T_LIST[i][i]
    max_num = compare_max(max_num, sum_num)

    # \ 이쪽방향 대각선
    # 내가 필요한 부분 [0][4] [1][3] [2][2] [3][1] [4][0]
    reverse_diagonal_sum = 0
    for i in range(N):
        reverse_diagonal_sum += T_LIST[i][N-1-i]
    max_num = compare_max(max_num, sum_num)

    print('#{} {}'.format(test_case, max_num))




