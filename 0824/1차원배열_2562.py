import sys
sys.stdin = open('input_2562.txt', 'r')

# 백준 단계별 풀이 - 1차원 배열 - 2562 문제
# 최댓값이 어디에 있는지 찾는 문제

N = 9
max_num = 0
pos = 0

for i in range(1, N+1):
    number = int(input())
    if number > max_num:
        max_num = number
        pos = i

print('{}\n{}'.format(max_num, pos))