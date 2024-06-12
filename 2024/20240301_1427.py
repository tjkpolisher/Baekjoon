# 1427: 소트인사이드

# 1. N 입력
# 2. 정수 변환 없이 정렬 함수를 사용해 내림차순으로 정렬
# 3. 정수 변환 후 출력

N = input()
N = sorted(N, reverse=True)
print(int(''.join(N)))
