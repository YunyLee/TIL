import sys
sys.stdin = open('기지국_input.txt', 'r')

# 델타검색...

def check(x, y):
    for i in range(4): #4방향
        nx = x + dx[i]
        ny = y + dy[i]
        # 인덱스 체크, H일때 X로 바꾸기
        # 16진수 (A ~ F) ord(arr[i]) - ord('A') +10
        for j in range(ord(arr[x][y]) - ord('A')+1): # B랑 C작업을 위한.....???
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H' :#앞에 인덱스 체크 먼저해주고
            arr[nx][ny] = 'x'
            nx = nx + dx[i] #한번더가
            ny = ny + dy[i]


# B는 이 작업을 2번 해야된다.
# C는 이 작업을 3번 해야된다.

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 0
    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] =='C':
                check(i, j)

    # 4방향 돌려서 커버되는 H -> X
    # H 세기
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                ans += 1

    print('#{} {}'.format(tc, ans))

