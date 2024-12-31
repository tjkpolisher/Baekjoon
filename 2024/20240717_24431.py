# 24431: 유사 라임 게임
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘: 구현/자료 구조/문자열/정렬/해시를 사용한 집합과 맵/트리를 사용한 집합과 맵

# 1. 테스트 케이스의 수 T 입력 (1 ≤ T ≤ 10)
# 2. n, L, F 입력 (1 ≤ F ≤ L ≤ 10, 2 ≤ 500)
# 3. 길이 L인 문자열 n개 입력
# 4. 문자열의 -F번 인덱스부터 시작해 역순으로 임시 문자열 생성
# 5. 임시 문자열을 딕셔너리에 저장
# 6. 딕셔너리를 순회하면서 크기가 1보다 클 경우 결과값에 딕셔너리 값 // 2를 더함
# 7. 결과값 출력

T = int(input())

for i in range(T):
    dictionary = {}
    res = 0
    n, L, F = map(int, input().split())
    arr = list(input().split())

    for j in arr:
        tmp = j[-F:]
        if tmp in dictionary:
            dictionary[tmp] += 1
        else:
            dictionary[tmp] = 1

    for j in dictionary:
        if dictionary[j] > 1:
            res += dictionary[j] // 2
    print(res)
