# 1010: 다리 놓기
# 유의사항: 다리를 짓기 적합한 곳을 사이트라고 칭함. 0 < N <= M < 30
# 알고리즘 분류: 수학/다이나믹 프로그래밍/조합론

## 1. 테스트 케이스의 개수 T 입력
## 2. [반복문]
## 2-1. 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M 입력
## 2-2. 조합(mCn) 계산
## 2-3. 결과 출력

from math import comb
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    c = comb(M, N)
    print(c)
