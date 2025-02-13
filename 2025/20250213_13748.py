# 13748: Periodic Strings
# 특이사항: 다국어(영어)
# 출처: 2016 Southeast USA Regional Programming Contest Division 1 I번
# 알고리즘 분류: 문자열/브루트포스 알고리즘

# 1. 길이 1 이상 100 이하의 문자열 s 입력
# 2. 맨 앞부터 길이가 1인 문자열을 슬라이스 후 패턴 일치 확인
# 3. 패턴이 다른 문자열이 나오면 길이를 1씩 증가시키고, 문자열의 순서를 회전시키면서 그 문자열들이 패턴에 일치하는지 확인
# 4-1. 패턴이 일치하면 슬라이싱의 길이 k 출력
# 4-2. 패턴이 마지막까지 일치하지 않으면 문자열의 길이 출력

from collections import deque

s = input()
len_total = len(s)
for i in range(1, len_total // 2 + 1):
    sliced = s[:i]
    rotated = []
    deque_s = deque(sliced)
    for _ in range(i):
        rotated.append(''.join(deque_s))
        deque_s.rotate()

    for j in range(len_total // i):
        if s[i * j:i * (j + 1)] != rotated[j % i]:
            break
    else:
        print(i)
        exit()
print(len_total)
