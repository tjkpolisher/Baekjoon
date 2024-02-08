# 4158: CD
# 특이사항: 다국어(영어)(한국어 번역), 예제에 없는 다중 테스트 케이스에 유의

## 1. [반복문]
## 1-1. 두 사람이 가진 CD의 개수 N, M 입력
## 1-2. N줄에 걸쳐 상근이의 CD 번호 입력
## 1-3. M줄에 걸쳐 선영이의 CD 번호 입력
## 2. "0, 0"이 입력되면 실행 종료

import sys
input = sys.stdin.readline
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    cd_set = set()
    cnt = 0
    
    for _ in range(N):
        cd_set.add(int(input()))
    
    for _ in range(M):
        n = int(input())
        if n in cd_set:
            cnt += 1
    
    print(cnt)
