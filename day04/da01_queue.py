#da01_queue.py
#큐 자료구조 구현


#초기화 
SIZE = int(input('큐 크기입력 > '))
queue = [None for _ in range(SIZE)]
front = rear = -1 # rear는 마지막 데이터가 있는 위치(인덱스)의미함


#함수선언
def isQueueFull():
    global SIZE, queue, front, rear # 전역변수global은 def 함수내에서 값을 바꿀때나 사용할때 쓴다
    # 1. 가장 일반적 로직 
    # if rear == SIZE -1 :
    #     return True
    # else:
    #     return False
    
    #2. 개선된 로직
    if rear != SIZE -1:
        return False
    elif rear == SIZE -1 and front == -1: # 꽉찼음
        return True
    else:
        for i in range(front+1, SIZE): #i-1의 값에 front+1을 할당하는 것을 size까지 반복해라
            queue[i-1] = queue[i] # 데이터 앞 빈자리에 첫번째 데이터를 옮김
            queue[i] = None # i자라에는 None 될것이다
            
        front -= 1
        rear -= 1
        return False    

            

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is full')
    else:
        rear += 1
        queue[rear] = data
        

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty')
        return # 값이 없다
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data
    
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    else: 
        return queue[front + 1]
    

## 메인 모듈 
if __name__ == '__main__':
    while True:
        select = input('삽입(I) | 추출(E) | 확인(V) | 종료(Q) ---> ').upper()
        
        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
        elif select == 'E':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select == 'V':
            dat = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        else:
            print('입력오류')