# da02-1_practice(p453).py

#=== 선택 정렬과 퀵 정렬의 성능 비교하기 ===##
# 두 정렬 방식의 시간 차이 비교 예제

import random
import time


## 클래스와 함수 선언 부분 ##

# 선택 정렬 함수
def selectSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if(ary[minIdx] > ary[k]):
                minIdx = k 
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp
        
    return ary        

# 퀵 정렬 함수
def qSort(arr, start, end):
    if end <= start:
        return
    low = start
    high = end
    
    pivot = arr[(low + high) // 2] #작은 값은 왼쪽, 큰 값은 오른쪽으로 분리 => 중앙값 구함
    while low <= high: # 작은수가 높은 수보다 작거나 같을 때 까지 반복
        while arr[low] < pivot: # 중앙치보다 작을때 까지 반복
            low += 1 # 자리수 한칸씩 이동 
        
        while arr[high] > pivot: # 중앙갑보다 (현재) 수가 높을때까지 반복
            high -= 1 # 자리수 왼쪽으로 한칸씩 이동
        
        if low <= high: # (현재)수가 (비교대상)값보다 작거나 같다면
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low +1, high -1
        
    mid = low
    
    qSort(arr, start, mid-1) # 왼쪽정렬
    qSort(arr, mid, end) # 오른쪽 정렬
    


# def quickSort(ary):
#     qSort(ary, 0, len(ary)-1)
    
            

## 메인 코드 부분 ##

countAry = [1000, 10000, 12000, 15000]

for count in countAry:
    tempAry =[random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print(f"## 데이터 수 : {count}개")
    start = time.time()
    selectSort(selectAry)
    end = time.time()

    print(f"선택 정렬 ---> {end-start:>10.3f}초")
    start = time.time()
    # quickSort(selectAry)
    qSort(quickAry, 0, len(quickAry)-1)
    end = time.time()
    print(f"퀵 정렬 ---> {end-start:>10.3f}초")
    print()

    # count *= 5 # -->왜 필요함??? => countAry = [1000, 10000, 12000, 15000] 5배를 하면서 더 다양한 값을 출력하려고
