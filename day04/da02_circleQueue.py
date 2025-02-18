# da01_circleQueue.py (263Pg)


# 함수선언부분 
def isQueueFull():
    global SIZE, queue, front, rear
    if((rear+1) % 5 == front) :
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐가 꽉 찼습니다')
        return
    # 큐가 차지 않고 데이터를 넣을 수 있다면
    rear = (rear+1) % SIZE
    queue[rear] = data

# 삭제    
def deQueue():
    global SIZE, queue, front, rear
    #큐가 비었는데 삭제하려고 할때
    if (isQueueEmpty()):
        print('큐가 비었습니다')
        return None
    #큐에 데이터가 있는 상태에서 삭제하려고 할때
    front = (front + 1) % SIZE 
    data = queue[front]
    queue[front] = None
    return data


# 확인
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 비었습니다')
        return None
    
    #큐가 있는 경우
    return queue[(front + 1) % SIZE]

        
    
# 전역변수 선언
SIZE = int(input('큐 크기를 입력해주세요 >'))    
queue = [None for _ in range(SIZE)]
front = rear = 0

# 메인
if __name__ == '__main__':
    
    while True:
        select = input('삽입(I) | 추출(E) | 확인(V) | 종료(Q)').upper()
        if select == 'I':
            data = input('입력할 데이터 > ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
            print(f'front : {front}, rear : {rear}')
            print()
        elif select == 'E':
            data = deQueue()
            print(f'추출된 데이터 : {queue}')
            print(f'큐 상태 : {queue}')
            print(f'front : {front}, rear : {rear}')
        elif select == 'V':
            data = peek()
            print(f'확인된 데이터 : {data}')
            print(f'큐 상태 : {queue}')
            print(f'front : {front}, rear : {rear}')
        elif select == 'Q':
            break
        else:
            print('입력 오류')
    
print('프로그램 종료')
            
            