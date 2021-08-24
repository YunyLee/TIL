import sys
sys.stdin = open('input_8958.txt', 'r')

# 백준 단계별 풀이 - 1차원 배열 - 8958 문제
# OX 퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산하는 문제

TC = int(input())

for test_case in range(TC):
    SENTENCE = input()
    result_sum = 0
    cnt = 1

    for i in SENTENCE:
        if i == 'O':
            result_sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(result_sum)