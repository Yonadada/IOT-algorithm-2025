#da03_stack.py
#스택 동작확인 구현

# 반복문에서 i를 쓰지 않는 경우 _(언더바)변경 가능
SIZE = int(input('Stack 크기를 결정해주세요 > '))
stack = [None for _ in range(SIZE)] # 결과값 => [None, None, None, None, None]
top = -1 # stack이 비워져 있음 => -1

## 함수 선언
def isStackFull(): #스택이 꽉 차있는지 확인하는 함수
    global SIZE, stack, top
    
    if (top == SIZE - 1): # Full / 실무에서 쓰는 스택은 거의 무제한이다
        return True
    else:
        return False

def isStackEmpty(): # 스택이 비었는지 확인하는 함수
    global SIZE, stack, top
    
    if (top == -1) : # Empty
        return True
    else:
        return False
    

def push(data): # 데이터 스택에 추가
    global SIZE, stack, top
    
    if isStackFull(): # isStackFull() == True와 동일
        print('Stack is Full')
        # return 생략 
    else:
        top += 1
        stack[top] = data
        
def pop(): # 스택에서 데이터 추출 
    global SIZE, stack, top

    if isStackEmpty():
        print('Stack is Empty')
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
    
def peek(): # 스택의 top위치의 데이터 확인(살짝보기)
    global SIZE, top, stack
    if isStackEmpty(): 
        print('Stack is Empty')
        return None
    else:
        return stack[top]
    
    
## main 
if __name__ =='__main__':
    
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q) > ').upper()
        if select == 'Q': break
        elif select == 'I': 
            data = input('입력데이터 > ')
            push(data)
            print(f'스택상태\n{stack}')
        elif select == 'E':
            data = pop()
            print(f'추출데이터 > {data}')        
            print(f'스택상태\n{stack}') 
        elif select == 'V':
            data == peek()
            print(f'추출데이터 > {data}')        
            print(f'스택상태\n{stack}') 
        
        else:
            print('---입력오류---')
print('스택종료!!!!')