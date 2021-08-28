import sys
sys.stdin = open('input_4834.txt', 'r')

# SWea - Learn- Course - List1 - 숫자카드(4834)

TC = int(input())

for test_case in range(1, TC+1):
    N = int(input())
    NUM_LIST = [int(i) for i in input()]

    # 변수 초기화
    check_list = [0] * 10
    best_num = 0
    cnt = 0

    # check_list에서 각 번호에 맞는 자리에 1씩 더해주고,
    for i in NUM_LIST:
        check_list[i] += 1

    for i in range(len(check_list)):
        if check_list[i] == max(check_list):
            best_num = i
            cnt = max(check_list)

    print('#{} {} {}'.format(test_case, best_num, cnt))

