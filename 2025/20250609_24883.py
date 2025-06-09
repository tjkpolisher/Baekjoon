# 24883: 자동완성
# 출처: 2022 숭고한 연합 알고리즘 콘테스트 Division 2 A번
# 알고리즘 분류: 구현

# 1. 알파벳 하나 입력
# 2. N 또는 n 이면 "Naver D2", 아니면 "Naver Whale" 출력

alphabet = input()

if alphabet in ("N", "n"):
    print("Naver D2")
else:
    print("Naver Whale")
