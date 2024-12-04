# 16506: CPU
# 출처: 충남대학교 제2회 생각하는 프로그래밍 대회 D번
# 알고리즘 분류: 구현

# 1. 명령어의 개수 N 입력 (1 ≤ N ≤ 500)
# 2. N개의 줄에 걸쳐 명령어가 어셈블리어 코드 opcode rD rA rB 또는 opcode rD rA #C 형식으로 주어짐
# [보충설명] 명령어(opcode)는 항상 대문자, rD/rA/rB는 레지스터 번호(0 ≤ rD, rA, rB ≤ 7)
# [보충설명] 레지스터는 사용하지 않을 경우에만 0이 주어짐. 정수 #C(0 ≤ #C ≤ 15)는 상수를 의미.
# [보충설명] opcode가 C로 끝나면 #C를 사용하고, 그렇지 않으면 rB를 연산에 사용.
# 3. opcode가 C로 끝나면 입력받은 명령어 중 마지막 숫자를 C로 지정
# 4. opcode를 기계어 비트 딕셔너리를 참조해 변환하고, opcode가 C로 끝나면 4번 비트를 1로 지정, 그렇지 않으면 0으로 지정
# 5. 반드시 0으로 지정되는 5번 비트를 정답 리스트에 추가
# 6. rD를 3비트 이진수로 변환하여 리스트에 추가
# 7. rA를 3비트 이진수로 변환하되, opcode가 MOV/MOVC/NOT일 경우 000 추가
# 8-1. opcode가 C로 끝날 경우 #C를 4비트 이진수로 변환하여 리스트에 추가
# 8-2. 그렇지 않을 경우 rB를 3비트 이진수로 변환하고 마지막에 0을 추가해 리스트에 추가
# 9. 변환된 기계어 코드 리스트를 단일 문자열로 병합해 출력

import sys
input = sys.stdin.readline

N = int(input())
# opcode를 기계어 비트로 변환하는 딕셔너리
opcode_table = {'ADD': '0000', 'SUB': '0001', 'MOV': '0010', 'AND': '0011',
                'OR': '0100', 'NOT': '0101', 'MULT': '0110', 'LSFTL': '0111',
                'LSFTR': '1000', 'ASFTR': '1001', 'RL': '1010', 'RR': '1011'}

for _ in range(N):
    opcode, rD, r1, r2 = input().rstrip().split()
    rD = int(rD)
    rA = int(r1)
    if opcode[-1] == 'C':
        C = int(r2)
    else:
        rB = int(r2)

    ans = []
    # opcode 변환
    if opcode[-1] == 'C':
        ans.append(opcode_table[opcode[:-1]])
        ans.append('1')
    else:
        ans.append(opcode_table[opcode])
        ans.append('0')

    # 5번 비트는 항상 0
    ans.append('0')

    # rD 변환
    rD = bin(rD)[2:]
    if len(rD) < 3:
        rD = '0' * (3 - len(rD)) + rD
    ans.append(rD)
    # rA 변환
    if opcode[:3] == 'MOV' or opcode[:3] == 'NOT':
        rA = '000'
    else:
        rA = bin(rA)[2:]
        if len(rA) < 3:
            rA = '0' * (3 - len(rA)) + rA
    ans.append(rA)

    # rB, #C 변환
    if opcode[-1] == 'C':
        C = bin(C)[2:]
        if len(C) < 4:
            C = '0' * (4 - len(C)) + C
        ans.append(C)
    else:
        rB = bin(rB)[2:]
        if len(rB) < 3:
            rB = '0' * (3 - len(rB)) + rB
        ans.append(rB)
        ans.append('0')

    # 병합 후 출력
    print(''.join(ans))
