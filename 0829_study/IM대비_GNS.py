import sys
sys.stdin = open('input_1221.txt', 'r')

# 0813 hw GNS - 1221

TC = int(input())
english_num = ['ZRO''ONE''TWO''THR''FOR''FIV''SIX''SVN''EGT''NIN']
for test_case in range(1, TC+1):

    T_NUM, N = map(str, input().split())
    N_LIST = list(map(str,input().split()))
    result_lst = []

    for i in N_LIST:
        for j in range(len(english_num)):
            if i == english_num[j]:
                


    # print(T_NUM)
    # print(result_lst)
