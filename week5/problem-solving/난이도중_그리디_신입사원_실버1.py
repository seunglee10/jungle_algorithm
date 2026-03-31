# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

# 체스트 케이스 개수
t = int(input())

# 지원자의 숫자
for _ in range(t):
    n = int(input())

    # print(document_score)   #3
    # print(interview_score)  #2

    # 서류 순위, 면접 순위 쌍으로 묶인 튜플 만들기
    people = []
    for i in range(n):
        # 지원자의 서류 성적 순위, 면접 성적 순위
        document_score, interview_score = map(int, input().split())
        people.append((document_score, interview_score))

        # print(people)  # [(3, 2), (1, 4), (4, 1), (2, 3), (5, 5)]

    # 서류 순위 기준으로 오름차순
    people.sort()
    # print(people)   # [(1, 4), (2, 3), (3, 2), (4, 1), (5, 5)]

    # [0]은 서류 1등이니까 무조건 뽑힘, 기준이 됨
    # count = 합격한 사람
    count = 1
    passed_people = people[0][1]
    # 서류 2등부터 for문 돌려서 면접 순위 비교
    # 숫자 작을 수록 순위 높아서 뽑히는거임
    for i in range(1, n):
        if people[i][1] < passed_people:
            passed_people = people[i][1]
            count += 1
    print(count)
