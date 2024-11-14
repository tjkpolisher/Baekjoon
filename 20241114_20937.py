# 20937: 떡국
# 출처: 2021 신촌지역 대학생 프로그래밍 대회 동아리 연합(SUAPC) 겨울 대회 B번
# 알고리즘 분류: 그리디 알고리즘/애드 혹

# 1. 떡국 그릇의 개수 N 입력 (1 ≤ N ≤ 500,000)
# 2. 떡국 그릇들의 크기 c_i를 N개 입력 후 리스트에 저장 (1 ≤ c_i ≤ 50,000)
# [보충설명] 모든 입력 데이터는 정수로 주어짐
# 3. 각 원소들을 순회하면서 원소들의 개수를 저장
# 4. 원소들의 개수의 최대값을 출력

from collections import Counter

N = int(input())
plates = list(map(int, input().split()))
counter_plates = Counter(plates)
print(counter_plates)
print(max(counter_plates.values()))
