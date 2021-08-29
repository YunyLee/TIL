import sys
sys.stdin = open('input_4843.txt', 'r')

# SWEA - Learn- Course - List2 - 특별한정렬(4843)

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input()) # N개의 정수
    NUMBERS = list(map(int,input().split()))
    special_list = [0] * N

    # 오름차순
    up = sorted(NUMBERS)
    down = sorted(NUMBERS, reverse=True)

    for i in range(N):
            if i%2 == 0:
                special_list[i] = down.pop(0) #맨 앞에꺼 빼서 이 값에 넣자
            if i%2 ==1:
                special_list[i] = up.pop(0)
    result = ''
    for i in range(10): #10개만 출력해라
        result += str(special_list[i]) + ' '

    print('#{} {}'.format(test_case, result))