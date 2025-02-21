# da01_image_process.py
# 이미지 처리(정렬 알고리즘)

from tkinter import *

# 앞에 구현한 퀵소트 그대로 복붙
def sortQuickN(ary,start,end):
    
    if end <= start: return # 재귀호출 종료 조건
    low = start; high = end 
    
    pivot = ary[(low + high) // 2] # 리스트 중간값을 기준값으로 
    while low <= high:
        while ary[low] < pivot:
            low += 1
        while ary[high] > pivot:
            high -= 1
        if low <= high:
            ary[low], ary[high] = ary[high], ary[low]
            low, high = low + 1, high - 1
            
    
    sortQuickN(ary, start, low-1 ) # 왼쪽 그룹 다시 정렬(재귀호출)    
    sortQuickN(ary, low, end) # 오른쪽 그룹 다시 정렬(재귀호출)
    


root = Tk() # tkinter.Tk() --> 줄이려고 
root.geometry('600x600')
root.title('이미지처리(정렬)')

photo = PhotoImage(file='./image/cupDog.png')

photoAry = []
h = photo.height() # 사진 높이 600
w = photo.width() # 넓이 600
for i in range(h): # 행렬 row 동일
    for k in range(w): # 행렬 col 동일
        r, g, b = photo.get(i, k)
        value = (r + g + b) // 3  #평균치 => rgb셋다 숫자 동일해서 //3 해도 1개의 값이 나옴
        photoAry.append(value)

print(len(photoAry)) # 360000 리스트가 생성됨

# 퀵소트로 정렬
dataAry =photoAry[:]
sortQuickN(dataAry, 0, len(dataAry)-1)
midValue = dataAry[h*w // 2] #중앙값 찾기

# 색상들을 정리. 중간값보다 작으면 검은색, 중간값보다 크면 흰색
for i in range(len(photoAry)):
    if photoAry[i] <= midValue:
        photoAry[i] = 0 #black
    else:
        photoAry[i] = 255 #white

# 흑백이미지로 변경 
pos = 0
for i in range(h):
    for k in range(w):
        r = g = b = photoAry[pos]
        pos += 1
        photo.put(f'#{r:02x}{g:02x}{b:02x}', (i,k)) 
        # photo의 각 위치에 있는 색상을 photoAry에 들어있는 값으로 변경하겠다
        
paper = Label(root, image=photo)
paper.pack(expand=1, anchor=CENTER)


root.mainloop()