strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#

strs.sort()
print(strs)  # ['ate', 'bat', 'eat', 'nat', 'tan', 'tea']
# 출력: [["bat"],["nat","tan"],["ate","eat","tea"]]

arr = [[],[],[]]
for str in strs:
    if "b" in str:
        arr[0].append(str)
    # elif str in
    elif "n" in str:
        arr[1].append(str)
    elif "e" in str:
        arr[2].append(str)
print(arr)



for str in strs:
    for s in str:
        num = sum(ord(s))
    # 여기에서 나온 num을 해시테이블의 키로 잡아서 밸류에 집어넣으면 되지 않을까 생각했는데 모르겠다