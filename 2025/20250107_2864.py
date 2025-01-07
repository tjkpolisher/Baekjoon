# 2864: 5와 6의 차이
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: COCI 2010/2011 Contest #3 2번
# 알고리즘 분류: 수학/그리디 알고리즘/문자열/사칙연산

# 1. 두 정수 A, B 입력 (1 ≤ A, B ≤ 1000000)
# 2. A와 B의 각 자릿수를 모두 5로 바꾼 수와 모두 6으로 바꿈
# 3. 각각의 경우에 대해 합을 구함
# 4. 3에서 구한 두 합을 출력

A, B = input().split()
A_5 = A.replace('6', '5')
B_5 = B.replace('6', '5')
sum_min = int(A_5) + int(B_5)
A_6 = A.replace('5', '6')
B_6 = B.replace('5', '6')
sum_max = int(A_6) + int(B_6)
print(sum_min, sum_max)
