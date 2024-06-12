# 1380: 귀걸이
# 특이사항: 다국어(영어)(한국어 번역)
# 알고리즘 분류: 구현/문자열

## 1. 0을 입력하면 종료. 그렇지 않으면 귀걸이 압수당한 여학생 수 n 입력.
## 2. n줄에 걸쳐 여학생 이름 입력 후 리스트에 저장.
## 3. 2n-1줄에 걸쳐 여학생 번호와 'A' 또는 'B'를 스택에 입력.
## 3-1. 스택에 서로 다른 A와 B가 있을 경우 키 삭제.
## 4. 숫자 하나만 입력받으면 해당 시나리오 번호 및 학생 이름 출력 후 다음 루프로 진행.

scene_num = 0
while True:
    scene_num += 1
    n = int(input())
    if n == 0:
        break

    names = []
    for _ in range(n):
        names.append(input())
    index_stack = dict()

    for i in range(2 * n - 1):
        idx, c = input().split()
        idx = int(idx)
        if idx not in index_stack:
            index_stack[idx] = [c]
        else:
            index_stack.pop(idx, None)

    i = list(index_stack.keys())[0]
    print(scene_num, names[i - 1])
