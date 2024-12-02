# 13243: Non-decreasing subsegment
# 특이사항: 다국어(영어)
# 출처: 2016 AIPO National Finals 4번
# 알고리즘 분류: 구현

# 1. 리스트의 크기 n 입력 (1 ≤ n ≤ 10^5)
# 2. n개의 정수를 입력받아 리스트에 저장 (정수는 1 이상 10^9 이하)
# 3. 리스트의 맨 앞부터 순회하면서 단조 증가 여부를 확인
# 3-1. 다음 정수가 현재 정수보다 작을 경우, 리스트 크기 갱신 및 현재까지의 합 갱신
# 3-2. 그렇지 않을 경우 현재 부분수열의 크기와 그 원소의 합을 저장
# 4. 부분 수열의 길이와 그 합 출력

n = int(input())
integers = list(map(int, input().split()))

segment_len = 0  # 부분 수열의 크기
segment_sum = 0  # 부분 수열의 합
temp_len = 1
temp_sum = integers[0]

for i in range(1, n):
    if integers[i - 1] <= integers[i]:
        temp_len += 1
        temp_sum += integers[i]
    else:
        if segment_len < temp_len:
            segment_len = temp_len
            segment_sum = temp_sum
        temp_sum = integers[i]
        temp_len = 1

if temp_len > segment_len:
    segment_len = temp_len
    segment_sum = temp_sum

print(segment_len, segment_sum)
