class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # path = "/home/user/Documents/../Pictures"
        path = path.split("/")
        for file in path:
            # if .이거나 빈 문자열이면 무시
            if file == "." or file == "":
                continue
            # elif ..을 만나면 stack.pop()
            elif file == "..":
                # "/.."/인 경우 무시하는 조건 추가해줘야함
                if stack:
                    stack.pop()
            else:
                stack.append(file)
        return "/" + "/".join(stack)
