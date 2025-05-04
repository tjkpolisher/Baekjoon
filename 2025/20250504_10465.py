# 10465: Rolling Encryption
# 특이사항: 다국어(영어)
# 출처: Waterloo's local Programming Contests - 20 September, 2014 B번
# 알고리즘 분류: 구현/문자열

# 1. 정수 k 입력 (1 ≤ k ≤ 10,000)
# 2. c개의 문자로 구성된 문자열 입력 (1 ≤ c ≤ 100,000)
# 3. 문자열의 맨 앞 k개의 문자를 분리해 정답 리스트에 append
# 4. 3에서 분리한 문자열 중 가장 자주 등장한 문자의 알파벳 순서를 기록
# [보충설명] 개수가 같다면 문자열에서 먼저 등장한 알파벳을 우선 적용
# 5. 기록한 순서만큼 문자열에 남은 문자를 뒤로 이동(ord 함수 이용)
# 5-1. 단, 순서가 알파벳 소문자의 범위를 벗어날 경우 26을 빼고 변환
# 6. 이동시킨 각 문자를 정답 리스트에 append
# 7. 정답 리스트를 join하여 출력

k = int(input())
string = input()

n = len(string)
if n <= k:
    print(string)
    exit()

ans = []
ans.append(string[:k])

freq = [0] * 26
for i in range(k):
    freq[ord(string[i]) - ord('a')] += 1

for i in range(k, n):
    max_cnt = max(freq)
    for idx in range(26):
        if freq[idx] == max_cnt:
            shift = idx + 1
            break

    orig_idx = ord(string[i]) - ord('a')

    enc_idx = (orig_idx + shift) % 26
    ans.append(chr(enc_idx + ord('a')))
    if i - k >= 0:
        out_idx = ord(string[i - k]) - ord('a')
        freq[out_idx] -= 1
    freq[orig_idx] += 1

print(''.join(ans))
