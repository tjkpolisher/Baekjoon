# 9322: 철벽 보안 알고리즘
# 특이사항: 다국어(영어)(한국어 번역)
# 출처: ICPC Benelux Algorithm Programming Contest(BAPC) 2013 Preliminaries E번
# 알고리즘 분류: 자료 구조/문자열/해시를 사용한 집합과 맵

# 1. 테스트 케이스의 개수 입력 (100 이하의 정수)
# 2. 한 문장의 단어 수 n 입력 (1 ≤ n ≤ 1,000)
# 3. 제1공개키 입력 (문장에서 최대 한 번만 사용된 단어들로 구성)
# 4. 제2공개키 입력 (제1공개키의 단어들을 재배치하여 구성)
# 5. 암호문 입력 (제2공개키를 만든 규칙의 반대로 평문을 재배치하여 구성됨)
# 6. 제2공개키의 각 원소가 제1공개키의 몇 번 인덱스에 대응되는지를 저장
# 7. 해당 인덱스 변환에 맞게 암호문을 재배치하여 평문 구성
# 8. 평문 구성

T = int(input())
for _ in range(T):
    n = int(input())  # 한 문장의 단어 수
    first_key = list(input().split())  # 제1공개키
    second_key = list(input().split())  # 제2공개키
    code = list(input().split())  # 암호문

    mapping = [0] * n  # 제2공개키와 제1공개키의 인덱스 매핑
    for i in range(n):
        idx_orig = first_key.index(second_key[i])
        mapping[idx_orig] = code[i]
    print(' '.join(mapping))
