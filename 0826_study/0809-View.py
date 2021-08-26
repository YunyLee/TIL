import sys
sys.stdin = open('input_1206.txt', 'r')

def my_min(a, b, c, d):
    min_num = a
    if a < min_num:
        min_num = a
    if b < min_num:
        min_num = b
    if c < min_num:
        min_num = c
    if d < min_num:
        min_num = d

    return min_num

TC = 10

for test_case in range(1, TC+1):
    TEST_LENGTH = int(input())
    TEST_LIST = list(map(int, input().split()))

    cnt = 0
    for i in range(2, TEST_LENGTH - 2):
        view_1 = TEST_LIST[i] - TEST_LIST[i-2]
        view_2 = TEST_LIST[i] - TEST_LIST[i-1]
        view_3 = TEST_LIST[i] - TEST_LIST[i+1]
        view_4 = TEST_LIST[i] - TEST_LIST[i+2]

        if view_1 >0 and view_2>0 and view_3>0 and view_4 >0 :
            cnt += my_min(view_1, view_2, view_3, view_4)

    print('#{} {}'.format(test_case, cnt))
