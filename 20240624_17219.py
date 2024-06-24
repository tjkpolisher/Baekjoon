# 17219: 비밀번호 찾기
# 출처: 한양대학교 ERICA 캠퍼스 2019 HEPC MAVEN League F번
# 알고리즘 분류: 자료 구조/해시를 사용한 집합과 맵

# 1. 저장된 사이트 주소의 수 N, 비밀번호를 찾으려는 사이트 주소의 수 M 입력 (1 ≤ N ≤ 100,000, 1 ≤ M ≤ 100,000)
# 2. N개의 줄에 걸쳐 사이트 주소와 비밀번호 입력받아 딕셔너리에 저장(각각 최대 20자)
# [보충설명] 사이트 주소는 알파벳 대소문자, 대시(-), 마침표(.)로 구성되며 중복 없음. 비밀번호는 알파벳 대문자로만 구성.
# 3. M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소 입력(이미 저장된 사이트 주소만 입력됨)
# 4. 입력받은 사이트 주소를 딕셔너리에 키로 입력해 패스워드를 반환 후 출력

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site_password = {}
for _ in range(N):
    site, password = input().rstrip().split()
    site_password[site] = password

for _ in range(M):
    site = input().rstrip()
    print(site_password[site])
