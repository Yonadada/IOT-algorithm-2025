# da03-1_min_cost_spanningTree(355pg).py

# 전역변수 
G1 = None
storeAry =[['GS25', 30],['CU',60],['seven11',10],['miniStop',90],['eMart', 40]]
GS25,CU,seven11,miniStop,eMart = 0,1,2,3,4
SIZE = len(storeAry)

# 클래스 
class Graph():
    def __init__(self, size):
        self.SIZE = size 
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
    

def printGraph(g):
    print(' ', end=' ')
    for v in range(g.SIZE): # vertex로 인덱스를 나타냄 -> 정점의 이름을 가져와서 출력
        print("%9s" % storeAry[v][0], end=' ') 
    print()
    
    for row in range(g.SIZE): # 현재 행의 인덱스(row)
        print("%9s" % storeAry[row][0], end=' ')
        for col in range(g.SIZE): # 나머지 col은 인접행렬의 값(가중치)
            print("%8d" % g.graph[row][col], end=' ')
        print()
    print()

# 메인
# GS25:0, CU:1, sevenEleven:2, miniStop:3, eMart:4 

G1 = Graph(SIZE)

G1.graph[GS25][CU] = 1; G1.graph[GS25][seven11] = 1
G1.graph[CU][GS25] = 1; G1.graph[CU][seven11] = 1; G1.graph[CU][miniStop] = 1
G1.graph[seven11]

