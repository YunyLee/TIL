import sys
sys.stdin = open('input_4828.txt', 'r')

TC = int(input())
for test_case in range(1, TC+1):
    T_NUM = int(input())
    NUM_LIST = list(map(int, input().split()))

    max_num = 0
    min_num = 1000000
    for i in NUM_LIST:
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i
    result = max_num - min_num

    print('#{} {}'.format(test_case, result))