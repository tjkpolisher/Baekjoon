# 9850: Cipher
# 특이사항: 다국어(영어)
# 출처: National Olympiad in Informatics (Singapore) 2007 3번
# 알고리즘 분류: 구현/문자열/브루트포스 알고리즘

# 1. 암호화된 문자열 입력 (길이는 1000자 이내, 모든 문자는 대문자)
# 2. 암호문의 각 문자를 아스키 코드 십진수로 변환
# 2-1. 문자가 알파벳 대문자의 범위에 해당하면 번호에서 p를 뺌
# 2-2. 단, 65보다 작아지면 26을 더해줌
# 2-3. 해당되지 않을 경우 그대로 두기
# 2-4. 변환 또는 변환되지 않은 문자를 리스트에 저장
# 2-5. 리스트를 문자열로 바꿨을 때 'CHIPMUNKS'와 'LIVE'가 포함되면 루프 종료
# 2-5-1. 그렇지 않으면 p에 1을 더하여 다시 실행
# 3. 정답 문자열을 출력

ciphertext = input()

p = 1
while True:
    ans = []
    for c in ciphertext:
        num = ord(c)
        if 65 <= num < 92:
            num -= p
            if num < 65:
                num += 26
            new_c = chr(num)
            ans.append(new_c)
        else:
            ans.append(c)
    ans_string = ''.join(ans)
    if 'CHIPMUNKS' in ans_string and 'LIVE' in ans_string:
        break
    p += 1

print(ans_string)
