# 11008: 복붙의 달인
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Taiwan Online Programming Contest (TOPC) 2015 C번
# 알고리즘 분류: 구현/문자열

# 1. 테스트 케이스의 개수 T 입력 (T ≤ 25)
# 2. 2개의 문자열 s와 p 입력 (최대 길이는 각각 10000, 100)
# 3. s와 p의 길이를 각각 ls, lp 변수로 저장
# 4. s의 맨 앞 글자부터 시작해 lp만큼 슬라이싱하면서 p와 일치하는지 확인
# 4-1. p와 일치하면 다음 인덱스를 lp만큼 증가시키고 반복
# 4-2. 그렇지 않으면 다음 인덱스를 1만큼 증가시키고 반복
# 5. 반복문이 끝날 때마다 타이핑 시간에 1을 더함
# 6. 타이핑 시간 출력

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s, p = input().rstrip().split()
    ls = len(s)
    lp = len(p)
    cnt = 0  # 타이핑 시간
    i = 0  # 인덱스
    while i < ls:
        string = s[i:i + lp]
        if string == p:
            i += lp
        else:
            i += 1
        cnt += 1
    print(cnt)
