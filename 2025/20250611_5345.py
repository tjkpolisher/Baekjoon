# 5345: PLU count
# 특이사항: 다국어(영어)
# 출처: PLU 2013 Novice 10번
# 알고리즘 분류: 구현/문자열

# 1. 입력받을 텍스트의 개수 n 입력
# 2. n개의 줄에 걸쳐 텍스트를 한 줄에 한 문장씩 입력(최대 길이 80)
# 3. 입력받은 텍스트를 모두 소문자로 변환
# 4. p를 발견 후 다음 l 탐색 - 탐색 후에는 해당 문자를 사용한 것으로 간주하고 그 다음 위치부터 탐색
# 5. l을 발견 후 다음 u 탐색 - 탐색 후에는 해당 문자를 사용한 것으로 간주하고 그 다음 위치부터 탐색
# 6. 3에서 5까지의 과정을 끝낸 뒤 p의 인덱스를 바꾸면서 반복 수행
# 7. 카운터 출력


import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip().lower()
    cnt = 0
    i = 0

    while i < len(s):
        if s[i] == 'p':
            # 'p' 발견 후, 다음 'l' 탐색
            j = i + 1
            while j < len(s) and s[j] != 'l':
                j += 1
            if j == len(s):
                break
            # 'l' 발견 후, 다음 'u' 탐색
            k = j + 1
            while k < len(s) and s[k] != 'u':
                k += 1
            if k == len(s):
                break

            cnt += 1
            i = k + 1
        else:
            i += 1

    print(cnt)
