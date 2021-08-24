import sys
sys.stdin = open('input_3052.txt', 'r')

# 백준 단계별 풀이 - 1차원 배열 - 3052 문제
# 서로 다른 값이 몇개인지 출력하는 프로그램

num_list = []
divided_list = []
result_list = []

for i in range(10):
    NUM = int(input())
    num_list.append(NUM)

for i in num_list:
    for j in range(10):
        divided_list.append(i%42)

for i in divided_list:
    if i not in result_list:
        result_list.append(i)

print(len(result_list))

# 중복되는 요소를 제거하는 set()함수를 이용하는 방법도 있다.
