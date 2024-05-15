# 1166: 선물
# 특이사항: 스페셜 저지
# 알고리즘 분류: 이진 탐색

# 1. 박스의 개수 N, 박스의 크기 L, W, H 입력
# [보충설명] 1 ≤ N ≤ 1,000,000,000 // 1 ≤ L, W, H ≤ 1,000,000,000
# 2. 0을 시작값, L, W, H 중 최대값을 끝값으로 설정해 이진 탐색 진행
# 2-1. 한 변의 길이가 mid인 상자 N개를 큰 박스에 넣을 수 있을 때를 기준으로 이진 탐색
# 3. mid를 출력

N, L, W, H = map(int, input().split())
start = 0
end = max(L, W, H)

for i in range(1000):
    mid = (start + end) / 2
    if (L // mid) * (W // mid) * (H // mid) >= N:
        start = mid
    else:
        end = mid

print(f"{end:.10f}")
