# 파이썬 자료구조와 알고리즘 147pg

#전역변수
memory =[]
head, pre, curr = None, None, None
dataArray = [['지민', '010-1111-1111'],['정국','010-2222-2222'],['뷔','010-3333-3333'],
            ['슈가','010-4444-4444'],['진','010-5555-5555']]

class Node():
    def __init__(self):
        self.data = None # 데이터(이름, 전화번호 저장)
        self.link = None # 다음 노드를 가리키는 포인터 
        
        
def printNodes(start):
    curr = start
    
    while curr is not None:
        print(curr.data, end='->')
        curr = curr.link
    print('None')    
    
    
def makeSimpleLinkedList(nameMobile):
    global memory, head, pre, curr
    printNodes(head) # 현재 리스트 출력 (디버깅용)
    
    # 첫번째 노드 삽입 
    node = Node()
    node.data= nameMobile  # 새 노드에 데이터 저장
    memory.append(node) # 리스트에 저장(메모리 관리용)
        
    if head == None: # 리스트가 비어있으면
        head = node # head를 새로운 노드로 설정
        return
    
    if head.data[0] > nameMobile[0]: # 삽입할 데이터가 현재 head보다 작다면 (이름순 정렬)
        node.link = head # 새 노드의 링크를 기존 head로 설정
        head = node # head를 새로운 노드로 변경
        return

# 메인
if __name__ == '__main__':
    
    for data in dataArray:
        makeSimpleLinkedList(data)
    
    
    printNodes(head)



