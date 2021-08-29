import sys
sys.stdin = open('input_4836.txt', 'r')

# SWEA - Learn- Course - List2 - 색칠하기(4836)

TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    board = [[0]*10 for _ in range(10)]
    purple = 0
    for i in range(N):
        X1, Y1, X2, Y2, COLOR = map(int, input().split())

        for row in range(X1, X2+1):
            for col in range(Y1, Y2+1):
                if board[row][col] == 1 and COLOR ==2:
                    board[row][col] = COLOR + 1
                    purple += 1
                if board[row][col] == 2 and COLOR ==1:
                    board[row][col] = COLOR + 2
                    purple += 1
                if board[row][col] == 0:
                    board[row][col] = COLOR

    print('#{} {}'.format(test_case, purple))