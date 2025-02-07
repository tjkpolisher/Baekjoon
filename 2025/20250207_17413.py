# 17413: 단어 뒤집기 2
# 알고리즘 분류: 구현/자료 구조/문자열/스택

# 1. 문자열 S 입력 (S의 길이는 100,000 이하)
# 2. 문자열을 순회하면서 '<>'로 둘러싸인 태그는 pass
# 2-1. '<'가 나오면 플래그를 True 처리, '>'가 나오면 플래그를 False 처리
# 3. 플래그가 False일 때 단어가 나오는 경우 다음 공백이 나올 때까지 단어를 체크
# 4. 체크한 단어를 역순으로 뒤집어서 원래 위치로 대체
# 5. 뒤집은 단어 출력
# 6. 마지막 문제까지 순회했으면 단어 리스트에 남아있는 문자들을 pop해서 출력

S = input()


def flag_check(flag):
    return not flag


tag_flag = False
length = len(S)
word_list = []  # 태그가 아닌 단어의 문자를 담을 리스트
for i, ch in enumerate(S):
    if ch in ('<', '>'):
        # 태그가 시작되거나 끝나면 플래그를 변환하고 태그 문자 출력
        tag_flag = flag_check(tag_flag)
        while word_list:
            print(word_list.pop(), end='')
        print(ch, end='')
    elif tag_flag:
        # 태그 안의 문자는 모두 그대로 출력
        print(ch, end='')
    else:
        if ch == ' ':
            # 공백 문자가 나오면 현재 word_list에 있는 문자를 모두 pop해서 출력
            while word_list:
                print(word_list.pop(), end='')
            print(' ', end='')
        else:
            # 그 외의 문자는 일단 word_list에 저장
            word_list.append(ch)
    if i == length - 1:
        # 마지막 문자까지 순회하면 word_list에 있는 문자를 모두 pop해서 출력
        while word_list:
            print(word_list.pop(), end='')
