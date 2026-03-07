"""
[파이썬 기본 문법 - 리스트와 딕셔너리 활용]

문제 설명:
- 학생들의 이름과 점수를 입력받아 평균 점수 이상인 학생들을 찾아 출력합니다.
- 파이썬의 기본 자료구조인 리스트와 딕셔너리를 활용하는 문제입니다.

입력:
- students: 학생 정보를 담은 딕셔너리 리스트
  예: [{"name": "Alice", "score": 85}, {"name": "Bob", "score": 92}]

출력:
- 평균 점수
- 평균 이상인 학생들의 이름 리스트

예제:
입력:
[
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 95}
]

출력:
평균 점수: 87.5
평균 이상 학생: ['Bob', 'David']

힌트:
- sum() 함수와 len() 함수를 활용하세요
- 리스트 컴프리헨션을 사용하면 간결하게 작성할 수 있습니다
"""


def find_above_average_students(students):
    """
    평균 점수 이상인 학생들을 찾는 함수

    Args:
        students: 학생 정보 딕셔너리 리스트

    Returns:
        tuple: (평균 점수, 평균 이상 학생 이름 리스트)
    """

    # # 1. 리스트를 순회해서 딕셔너리를 프린트 해보고싶음
    # for i in students:
    #     print(i)

    # # 2. 딕셔너리의 key인 score의 value인 점수를 꺼내오고 싶음
    # for dic in students:
    #     print(dic["score"])  # 85, 92, 78, 95

    # TODO: 모든 학생의 점수를 리스트로 추출하세요

    # 빈 배열 하나를 만들고 거기에 모든 학생의 점수를  append하기
    arr = []
    for student in students:
        arr.append(student["score"])
    # print(arr)  # [85, 92, 78, 95]

    # TODO: 평균 점수를 계산하세요

    # 평균 점수
    # 학생들의 총 합을 학생 수로 나눈 값
    # 학생들의 총 합 sum()
    # 총 학생 수 len()

    # print(sum(arr))  # 350
    # print(len(students))  # 4
    average = sum(arr) / len(students)
    # print(average)  # 87.5

    # TODO: 평균 이상인 학생들의 이름을 리스트로 추출하세요
    # 빈 리스트 하나 만들어서 조건을 만족하는 경우 거기에 append
    above_average_students = []
    for student in students:
        if student["score"] >= average:
            above_average_students.append(student["name"])
            # print(above_average_students)

    return average, above_average_students


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    students1 = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 92},
        {"name": "Charlie", "score": 78},
        {"name": "David", "score": 95},
    ]

    avg, students = find_above_average_students(students1)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")
    print()

    # 테스트 케이스 2
    students2 = [
        {"name": "Emma", "score": 70},
        {"name": "Frank", "score": 85},
        {"name": "Grace", "score": 90},
    ]

    avg, students = find_above_average_students(students2)
    print(f"평균 점수: {avg}")
    print(f"평균 이상 학생: {students}")
