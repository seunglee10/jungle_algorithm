"""
[연결 리스트 - Linked List 기본 구현]

문제 설명:
- 단순 연결 리스트를 구현합니다.
- 노드는 값과 다음 노드를 가리키는 포인터를 가집니다.

입력:
- 연결 리스트에 추가할 값들

출력:
- 연결 리스트의 모든 값 출력

예제:
입력: 1 -> 2 -> 3
출력: [1, 2, 3]

힌트:
- Node 클래스: data와 next 포인터
- LinkedList 클래스: head 포인터
- append(): 끝에 추가
- print_list(): 모든 노드 출력
"""

"""
1. 헤드를 넥스트노드에 저장한다
2. 넥스트노드의 넥스트가 없다면 순회를 끝낸다(끝까지 갔으니까)
3. 만약에 넥스트노드에 넥스트가 있다면 넥스트노드에 저장해준다(다음 노드로 넘어간다)
반복문을 돈게 끝까지 갔다는거니까
넥스트 노드가 끝 노드가 됐으니까 넥스트 노드의 넥스트에 뉴노드를 넣어준다
"""


# Node라는 클래스를 호출했을 때 그 안에 포함되어 있는 함수 실행하는 클래스를 만들꺼다
class Node:
    """연결 리스트의 노드"""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """단순 연결 리스트"""

    # self는 이름 넣어준다고 생각하면 됨
    def __init__(self):
        self.head = None

    def append(self, data):
        """리스트 끝에 노드 추가"""
        new_node = Node(data)

        # TODO: 리스트가 비어있으면 head를 new_node로 설정
        if not self.head:
            self.head = new_node
            return``

        # TODO: 마지막 노드 찾기
        last_node = self.head
        next_node = self.head.next
        while True:
            if not next_node:
                break
            last_node = next_node
            next_node = next_node.next

        # TODO: 마지막 노드의 next를 new_node로 설정
        last_node.next = next_node

    def print_list(self):
        """리스트의 모든 값 출력"""
        values = []

        # TODO: head부터 시작
        values.append(self.head.data)

        # TODO: 끝까지 순회하며 값 수집
        next_node = self.head.next
        while next_node:
            values.append(next_node.data)
            next_node = next_node.next

        return values


# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    print("=== 연결 리스트 테스트 ===")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    result = ll.print_list()
    print(f"리스트: {result}")
    print()

    # 테스트 케이스 2
    print("=== 연결 리스트 테스트 2 ===")
    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    ll2.append(40)
    result2 = ll2.print_list()
    print(f"리스트: {result2}")
