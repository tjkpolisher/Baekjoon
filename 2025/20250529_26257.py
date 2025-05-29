# 26257: std::shared_ptr
# 출처: SW마에스트로 제13기 알고리즘 대회 A번
# 알고리즘 분류: 구현/시뮬레이션

# 1. 객체의 개수 N, 포인터의 개수 M, 연산의 개수 Q 입력
# [보충설명] (1 ≤ N ≤ 2*10^5, N ≤ M ≤ 2*10^5, 1 ≤ Q ≤ 10^5)
# 2. M개의 줄에 걸쳐 i번 포인터가 가리키는 객체 번호 e_i 입력
# [보충설명] 0 ≤ e_i ≤ N, e_i = 0이면 포인터가 아무것도 가리키지 않음을 의미.
# 3. Q개의 줄에 걸쳐 수행할 연산 입력 (1 ≤ x_i,y_i ≤ M)
# 4. 주어진 연산에 따라 포인터 연산 수행
# 4-1. assign x y - 포인터 x는 기존 객체 대신 포인터 y가 가리키는 객체를 가리킨다
# 4-2. swap x y - 포인터 x와 포인터 y가 가리키는 객체를 서로 바꾼다
# 4-3. reset x - 포인터 x의 할당 해제
# 5. 모든 연산이 끝났을 때 소멸되지 않고 메모리에 남은 객체의 개수 K 출력
# 6. 다음 줄부터 남은 객체의 번호를 오름차순으로 출력

import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
pointers = {}
ref_count = {}

for i in range(1, M + 1):
    obj = int(input())
    pointers[i] = obj
    if obj > 0:
        ref_count[obj] = ref_count.get(obj, 0) + 1

for _ in range(Q):
    operation = input().rstrip()
    if operation.startswith("reset"):
        _, x = operation.split()
        x = int(x)

        old_obj = pointers[x]
        if old_obj > 0:
            ref_count[old_obj] -= 1
        pointers[x] = 0
    else:
        op, x, y = operation.split()
        x, y = int(x), int(y)
        if op == "assign":
            old_obj = pointers[x]
            new_obj = pointers[y]
            if old_obj > 0:
                ref_count[old_obj] -= 1
            if new_obj > 0:
                ref_count[new_obj] = ref_count.get(new_obj, 0) + 1
            pointers[x] = new_obj
        else:
            pointers[x], pointers[y] = pointers[y], pointers[x]

alive_objects = sorted([obj for obj, count in ref_count.items() if count > 0])
print(len(alive_objects))
if alive_objects:
    for obj in alive_objects:
        print(obj)
