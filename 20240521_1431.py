# 1431: 시리얼 번호
# 알고리즘 분류: 정렬

# 1. 기타의 개수 N 입력 (N ≤ 50)
# 2. N개의 줄에 걸쳐 시리얼 번호 입력 (길이는 최대 50, 알파벳 대문자 또는 숫자로만 구성, 중복 없음)
# 3. 시리얼 번호를 리스트에 입력
# 4. 시리얼 번호의 문자를 순회하면서 숫자인 경우 그 합을 저장하는 딕셔너리에 저장
# 5. 짧은 길이 먼저, 같은 길이 내에서는 번호 내의 숫자의 총합이 작은 순서대로 정렬 후, 그것도 똑같으면 사전 순으로 정렬
# 6. N개의 줄에 한 줄에 하나씩, 짧은 번호부터 시리얼 번호를 정렬한 결과 출력

import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
serial = []
serial_num_sum = defaultdict(int)
for _ in range(N):
    s_num = input().rstrip()
    temp = 0
    serial.append(s_num)
    for c in s_num:
        if c in "0123456789":
            temp += int(c)
    serial_num_sum[s_num] = temp

serial.sort(key=lambda x: (len(x), serial_num_sum[x], x))
for s in serial:
    print(s)
