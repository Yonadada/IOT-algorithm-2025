# day03_linear_list.py

# 선형리스트 일반구현
# 실제 파이썬이 이렇게 동작하는게 아니다!
# 배열(선형리스트)이 어떻게 동작하는지 로직을 파악할 것!

## 전역변수 선언 부분
katok = [] # 빈 배열
select = -1    # -1 : 통과 , 1 : 추가, 2 : 삽입,  3 : 삭제, 4 : 종료


# 
# 데이터 추가
def add_data(friend):
    katok.append(None)
    lenKatok =len(katok)
    katok[lenKatok - 1] = friend
    
# ---------------------------------------------
# 중간데이터 삽임 
# pos -> 삽입할 데이터 위치

def insert_data(pos,friend):
    #잘못된 인덱스를 넣었을 때 예외처리 필요
    if pos < 0 or pos > len(katok):
        print('실행할 범위를 벗어났습니다')
        return
        
    katok.append(None)      # 빈칸추가
    lenKatok = len(katok)
    
    for i in range(lenKatok - 1, pos, -1): # 추가할 위치까지 데이터를 뒤로 이동
        katok[i] = katok[i -1]
        katok[i -1] = None
        
    # 넣고자하는 데이터 삽입    
    katok[pos] = friend



#----------------------------------------------
# 마지막 값 삭제
# 데이터 삭제    

def delete_data(pos):
    if pos <0 or pos > len(katok) :
        print('삭제 범위를 벗어났습니다')
        return
    
    lenKato = len(katok)
    katok[pos] = None     # 지정된 위치 값을 삭제

    for i in range(pos+1, lenKato):
        katok[i -1] = katok[i] # i 값을 [i -1]에 대입
        katok[i] = None
            
    del(katok[lenKato - 1]) # 배열 맨마지막 삭제

#-----------------------------------
## 메인코드 영역 
if __name__ == '__main__':
    
    while True:
        select = int(input('선택( 1 : 추가, 2 : 삽입, 3 : 삭제, 4 : 종료 ) > '))
        
        if select == 1:
            data = input(' 추가 데이터 --> ')
            add_data(data)
            print(katok) 
            
        elif select == 2:
            pos,data = input('삽입할 위치, 데이터 입력 ---> ').split(',')
            pos = int(pos)
            
            insert_data(pos,data)
            print(katok)
            
        elif select == 3:
            pos = int(input('삭제위치 ---> '))
            delete_data(pos)
            print(katok)
            
        elif select == 4:
            break
        
        else:
            print('1 ~ 4중 입력해주세요')
            continue # 1 ~ 4 아닌것은 continue
#-----------------------------------


# add_data('다현')
# add_data('정현')
# add_data('쯔위')
# add_data('사나')
# add_data('지효')
# print(katok) # 중단점 2

    
# insert_data(2, '솔라')
# print(katok)
# insert_data(7, '문별')
# print(katok)

# print(katok)
# print(katok)

#======================
# 데이터 삭제

# lenKato = len(katok) # 중단점-----
# katok[3] = None     # 지정된 위치 값을 삭제

# for i in range(3+1, lenKato):
#     katok[i -1] = katok[i]
#     katok[i] = None
    
# del(katok[lenKato - 1]) # 배열 맨마지막 삭제
# print(katok)


