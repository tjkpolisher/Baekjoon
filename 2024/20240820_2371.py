# 2371: 파일 구별하기
# 알고리즘 분류: 구현/자료 구조/브루트포스 알고리즘/해시를 사용한 집합과 맵

# 1. 파일의 개수 N 입력 (1 ≤ N ≤ 100)
# 2. N개의 줄에 걸쳐 파일의 정보를 나타내는 자연수 입력(각 줄의 마지막에 -1 입력)
# 3. 입력받은 자연수를 리스트로 구성 후 앞에서부터 K개의 숫자를 확인
# 3-1. 만약 잘라낸 파일이 이미 전체 파일 리스트에 있을 경우, 모든 파일이 구분될 때까지 K를 증가
# 4. K 출력

N = int(input())
files = []
K = 1
for _ in range(N):
    files.append(list(map(int, input().split()[:-1])))


def check_distinguishable(K):
    seen = set()
    for file in files:
        truncated_file = tuple(file[:K])
        if truncated_file in seen:
            return False
        seen.add(truncated_file)
    return True


while not check_distinguishable(K):
    K += 1

print(K)
