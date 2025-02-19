# da02_dfs.py
# 그래프 깊이 우선탐색

# 전역변수
stack = []       # 스택
visitedAry = []  # 방문기록
G1 = None

# 그래프 클래스 
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        

## 메인코드
SIZE = 4 # 클래스의 size와 다름
G1 = Graph(4)
# 0:A, 1:B, 2:C, 3:D
# A ->
G1.graph[0][2] = 1
G1.graph[0][3] = 1

# B ->
G1.graph[1][2] = 1

# C ->
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1

# D ->
G1.graph[3][0] = 1
G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end=' ')
    print()
    
print("## dfs 시작 ##")

current = 0 # A에서 시작
stack.append(current) # 스택리스트에 push A
visitedAry.append(current) # 방문기록에는 A 적재

while len(stack) != 0: # stack의 길이가 0이 되면 모든 정점을 방문완료 했다는 의미
    next = None
    
    for vertax in range(SIZE):
        if G1.graph[current][vertax] == 1 : # 간선이 있다
            if vertax in visitedAry: # 이미 방문했으면 pass
                continue # pass도 가능
            else:
                next = vertax # 다음 번 방문할 정점 
                break
    
    if next != None: # 방문할 정점이 있으면
        current = next
        stack.append(current)
        visitedAry.append(current)
    else: 
        current = stack.pop()
            
print('방문순서', end='-->')
for i in visitedAry:
    print(chr(ord('A')+ i), end=' ')
# print()
# print(chr(ord('A'))) # A에 대한 ASCII 코드값 출력 -> 65