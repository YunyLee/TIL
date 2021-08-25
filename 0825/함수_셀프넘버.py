# 백준 단계별 풀이 - 함수 - 4673 문제
# 생성자가 없는 셀프넘버를 출력하는 프로그램

natural_number = set(range(1,10001))
generated_number = set()

for i in natural_number:
    a = i//10 #10의자리 100, 1000, 의자리 생각하기
    b = i%10 #1의자리
    generated_number.add(a+b+i)

result = sorted(natural_number-generated_number)
# print(natural_number)
# print(generated_number)
print(result)
