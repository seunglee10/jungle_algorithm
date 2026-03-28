class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        # 전체 좌표 False 처리
        # 전체 그리드 순회해야함. 섬이 하나 똘랑 하나 있는 경우 있을 수 있으니까
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    continue
                elif grid[i][j] == "1":
                    # 재방문 안하게 True로 방문처리
                    grid[i][j] = True

                    # 왼, 오, 위, 아래 탐색
                    # dx = [0,0,1,-1]
                    # dy = [1,-1,0,0]

                    # numIslands 이거 이대로 가져다쓰면 매개변수도 안맞고 그러니까 함수를 하나 만들어야함
                    search(i, j - 1)
                    search(i, j + 1)
                    search(i - 1, j)
                    search(i + 1, j)

                    # 탐색 끝내는 조건 들어가야 할 것 같음 -> 범위를 넘어가거나, 다음 탐색할 곳이 다 0이거나?

                    # 탐색 끝났으니까 count +1
                    count += 1

        return count
