import sys
sys.stdin = open('input_10818.txt', 'r')

# 백준 단계별 풀이 - 1차원 배열 - 10818 문제
# 최솟값과 최댓값을 찾는 문제

N = int(input())
N_LIST = list(map(int, input().split()))

max_num = N_LIST[0]
min_num = N_LIST[0]

for i in range(N):
    if N_LIST[i] > max_num:
        max_num = N_LIST[i]
    if N_LIST[i] < min_num:
        min_num = N_LIST[i]

print('{} {}'.format(min_num, max_num))

# max, min함수를 이용하면 print('{} {}'.format(min(N_LIST), max(N_LIST)))와 같이 간단하게도 풀 수 있다. 