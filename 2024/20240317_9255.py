# 9255: The Friend of My Enemy is My Enemy(번역: 적의 적은 내 친구)
# 특이사항: 다국어(영어)
# 알고리즘 분류: 구현/그래프 이론

# 1. 입력 데이터셋의 개수 K 입력
# 2. [반복문]데이터셋 양식
# 2-1. 첫 줄에 인적 네트워크에 있는 사람의 수 n, 사람들의 쌍 중 친구인 쌍의 개수 m 입력
# 2-2. m줄에 걸쳐 친구인 사람을 나타내는 두 정수 입력
# 2-3. 마지막 줄에 의심스러운 사람의 번호 s 입력
# 2-4. BFS를 실행해 s와 "직접" 커넥션이 있는 사람을 저장(오름차순으로 정렬 필요)
# 2-5. 문제에서 주어진 출력 양식에 맞게 결과 출력

K = int(input())
for x in range(1, K + 1):  # 데이터 세트 번호를 1부터 시작하도록 변경
    n, m = map(int, input().split())
    graph = dict()
    for _ in range(m):
        a, b = map(int, input().split())
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:  # 양방향 관계를 고려해 B->A도 추가
            graph[b] = [a]
        else:
            graph[b].append(a)

    s = int(input())
    connected = set()
    if s in graph:
        connected = set(graph[s])  # 직접적인 친구들을 추가

    # 친구 목록을 오름차순으로 정렬해 출력
    print(f"Data Set {x}:")
    print(' '.join(map(str, sorted(connected))))
    print()  # 데이터 세트 사이에 빈 줄 추가

