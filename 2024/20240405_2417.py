# 2417: 정수 제곱근
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 수학/이분 탐색

# 1. 정수 n 입력
# 2. 시작점은 0, 끝점은 n으로 설정
# 2. 중간점은 시작점 + 끝점 // 2로 우선 설정
# 3-1. 중간점의 제곱이 n보다 작으면 시작점을 중간점 + 1로 설정
# 3-2. 반대의 경우 끝점을 중간점 - 1로 설정
# 3-3. 시작점이 끝점보다 커질 경우 종료
# 4. 시작점 출력

n = int(input())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    if mid ** 2 < n:
        start = mid + 1
    else:
        end = mid - 1

print(start)
