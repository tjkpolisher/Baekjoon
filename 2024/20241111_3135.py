# 3135: 라디오
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: Croatian Highschool Competitions in Informatics 2007 Regional Competition - Juniors 1번
# 알고리즘 분류: 수학/그리디 알고리즘

# 1. 주파수를 뜻하는 두 정수 A, B 입력 (1 ≤ A, B < 1000, A ≠ B)
# 2. 즐겨찾기된 주파수의 개수인 정수 N 입력 (1 ≤ N ≤ 5)
# 3. N개의 줄에 걸쳐 즐겨찾기 주파수 입력
# 4. B와 A의 차이를 최소 버튼 누르는 횟수로 초기화
# 5. 즐겨찾기 주파수를 순회하면서 B와 해당 주파수의 차이를 기록
# 6. 기록해둔 차이와 최소 버튼 누르는 횟수 중 최소값으로 값을 갱신
# 7. 정답 출력

A, B = map(int, input().split())
N = int(input())
frequencies = []
for _ in range(N):
    frequencies.append(int(input()))

min_press = abs(B - A)

for freq in frequencies:
    press = 1 + abs(B - freq)
    min_press = min(press, min_press)

print(min_press)
