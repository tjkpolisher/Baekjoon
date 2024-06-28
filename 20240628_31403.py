# 31403: A + B - C
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: solved.ac Grand Arena #4 Division 2 A번
# 알고리즘 분류: 수학/문자열/사칙연산

# 1. 세 줄에 걸쳐 정수 A, B, C 입력
# 2. A, B, C를 수로 생각했을 때 A + B - C를 출력
# 3. A, B, C를 문자로 생각했을 때 int(str(A) + str(B)) - C를 출력

A = int(input())
B = int(input())
C = int(input())
print(A + B - C)
print(int(str(A) + str(B)) - C)
