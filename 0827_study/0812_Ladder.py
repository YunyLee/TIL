import sys
sys.stdin = open('input_1210.txt', 'r')

TC = 10
N = 100 # 100 * 100 2차원배열

TC = 1
N = 10 # 예시에서는 10*10

for test_case in range(1, TC+1):
    TC_NUM = int(input())
    BOARD = [list(map(int,input().split())) for _ in range(N)]

    x_start = []

    # 밑으로 내려가는 코드를 짜보자
    # y는 0으로 고정이고, x축만 쭉 돌면 된다.
    # 지금 밑에 코드는 2차원 배열을 다 보겠다는 뜻이다.
    for j in range(N):
        if BOARD[0][j] == 1:
            x_start.append(j)

    # 밑으로 가려면 BOARD[0][0] -> [1][0] -> [2][0]
    for j in range(N):
        for i in range(N):
            for k in x_start:
                if i==0 and j==k:
                    pass

    # 방이라고 생각
    # 11층에서 10층으로 내려가려 한다.
    # 현재위치 11 -> 현재위치 10
    # 현재위치라는 변수가 필요하다.

    # 2차원일때는 x와 y 변수 2개로 표현해야한다. (좌표 표현 몇층 몇호)
    # 어떤 값을 얻어오려면 두개으 ㅣ변수가 필요하다
    # 아래 내려간다? 좌표 2개지만 그중 y측 값만 바꿔줘야 한다.

    print('#{} {}'.format(test_case, x_start))
