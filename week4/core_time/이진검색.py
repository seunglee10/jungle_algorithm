# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # 루트가 없는 경우 -> 만약 루트가 None이면 []반환
        if root is None:
            return []

        # 결과 넣을 배열
        result = []

        # 시작 노드부터 일단 큐에 넣어야하니까 일단 집어넣기
        queue = deque([root])

        # 큐가 있는 경우 -> 큐에 있는걸 for 문으로 꺼내서 합하기?
        # for 문 돌려서 root[i]번째 값들의 합이랑 len(queue) 나누기?
        while queue:
            level_len = len(queue)
            level_sum = 0

            for i in range(level_len):
                node = queue.popleft()
                level_sum += node.val

                # 자식 노드들 있는 경우 넣어주고 싶음
                # 만약 왼쪽 있으면 큐에 왼쪽 넣고
                if node.left:
                    queue.append(node.left)
                # 만약 오른쪽 있으면 큐에 오른쪽 넣고
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_len)
        return result
