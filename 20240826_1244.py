# 1244: 스위치 켜고 끄기
# 출처: KOI 2000 초등부 2번
# 알고리즘 분류: 구현/시뮬레이션

# 1. 스위치 개수 N 입력 (N은 100 이하의 양의 정수)
# 2. 각 스위치의 상태가 1과 0으로 입력(켜져 있으면 1, 꺼져 있으면 0)
# 3. 학생 수 m 입력 (m은 100 이하의 양의 정수)
# 4. m개의 줄에 걸쳐 한 줄에 성별, 학생이 받은 수 입력
# [보충설명] 남학생은 1, 여학생은 2로 표시하고, 학생이 받은 수는 N 이하의 양의 정수
# 5-1. 남학생은 스위치 번호가 자기 수의 배수이면 스위치 상태 변경.
# 5-2. 여학생은 자기 수의 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간의 스위치 상태를 전부 변경.
# 6. 마지막 학생이 스위치 조작을 한 후 스위치 상태를 한 줄에 20개씩 출력

N = int(input())  # 스위치 개수
switches = [0] + list(map(int, input().split()))  # 스위치 상태, 인덱스 맞추기 위해 앞에 0 추가
m = int(input())  # 학생 수


def switch(n):
    return 0 if n == 1 else 1  # 스위치 상태를 반전시키는 함수


for _ in range(m):
    sex, number = map(int, input().split())
    if sex == 1:  # 남자
        # 남자는 받은 숫자의 배수에 해당하는 스위치들을 모두 반전시킨다.
        for i in range(number, N + 1, number):
            switches[i] = switch(switches[i])
    else:  # 여자
        # 여자는 자신이 받은 번호의 스위치를 먼저 반전시킨다.
        switches[number] = switch(switches[number])
        # 좌우 대칭을 검사하며 스위치를 반전시킨다.
        c1, c2 = number - 1, number + 1
        while c1 >= 1 and c2 <= N:
            if switches[c1] != switches[c2]:  # 대칭이 아니면 중단
                break
            switches[c1] = switch(switches[c1])
            switches[c2] = switch(switches[c2])
            c1 -= 1  # 왼쪽으로 한 칸 이동
            c2 += 1  # 오른쪽으로 한 칸 이동

# 스위치 상태를 20개씩 출력하기 위한 코드
switches = switches[1:]  # 인덱스 0을 제거하여 원래 스위치 리스트로 복구
for i in range(0, N, 20):
    print(*switches[i:i + 20])
