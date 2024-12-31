# 13333: Q-인덱스
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Daejeon Nationalwide Internet Competition 2016 I번
# 알고리즘 분류: 브루트포스 알고리즘/정렬

# 1. 학생이 발표한 논문의 수 n 입력 (1 ≤ n ≤ 1,000)
# 2. n개의 논문들에 대한 인용횟수를 공백으로 구분해 입력 (인용횟수는 0 이상 10,000 이하의 정수)
# 3. 인용횟수를 리스트에 저장 후 내림차순으로 정렬
# 4. 첫 번째 인덱스부터 순회하면서, 현재 인덱스보다 현재 원소가 적을 경우 q-인덱스 갱신
# 5. q-인덱스 출력

n = int(input())
citations = list(map(int, input().split()))
q_index = 0

citations.sort(reverse=True)
for i, k in enumerate(citations):
    if i + 1 <= k:
        q_index = i + 1

print(q_index)
