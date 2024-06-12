# 1417: 국회의원 선거
# 특이사항: 다솜이는 항상 기호 1번으로 지정됨.
# 다른 모든 사람의 득표수보다 많은 득표수를 가져야 당선
# 돈으로 매수된 사람은 반드시 다솜이에게 투표한다고 가정.

# 알고리즘 분류: 구현/자료 구조/그리디 알고리즘/시뮬레이션/우선순위 큐

## 1. 후보의 수 N 입력
## 2. N줄에 걸쳐 각 기호의 후보를 찍으려 하는 사람의 수 입력
## 3. [반복문] 기호 1번인 다솜이가 최대 득표를 받을 때까지 아래 절차 반복
## 3-1. 현재 최대 득표수가 유일한지 확인
## 3-1-1. 최대 득표수가 유일할 경우, 다솜이가 최대 득표인지 확인
## 3-1-1-1. 다솜이가 최대 득표일 경우 현재까지 매수한 사람의 수(cnt)를 출력 후 종료
## 3-1-1-2. 그렇지 않을 경우, 해당 기호의 득표수에서 1을 빼고 다솜이에게 1을 더한 뒤 매수한 사람 수 1명 추가
## 3-2. 현재 최대 득표수가 유일하지 않을 경우
## 3-2-1. 다솜이가 최대 득표수에 포함되지 않을 경우, 바로 다음 번호의 후보에게서 1을 빼고 다솜이에게 1을 더한 뒤 매수한 사람 1명 추가
## 3-2-2. 다솜이가 최대 득표수에 포함될 경우, 다솜이를 제외한 후보 중 한 명에게서 1을 빼고 다솜이에게 1을 더한 뒤 매수한 사람 1명 추가

N = int(input())
votes = []
for _ in range(N):
    votes.append(int(input()))

cnt = 0
while True:
    max_votes = max(votes)
    max_indices = []
    
    for i, v in enumerate(votes):
        if v == max_votes:
            max_indices.append(i)
        if len(max_indices) == votes.count(max_votes):
            break
    
    if len(max_indices) == 1:
        max_index = max_indices[0]
        if max_index == 0:
            print(cnt)
            break
        elif len(max_indices) == 1:
            votes[max_index] -= 1
            votes[0] += 1
            cnt += 1
    else:
        if 0 not in max_indices:
            max_index = max_indices[0]
        else:
            max_index = max_indices[1]
        
        votes[max_index] -= 1
        votes[0] += 1
        cnt += 1
