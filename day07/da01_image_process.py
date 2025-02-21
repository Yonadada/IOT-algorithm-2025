# da01_image_process.py
# 이미지 처리

from tkinter import *

root = Tk() # tkinter.Tk() --> 줄이려고 
root.geometry('600x600')
root.title('이미지처리')

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

# 색상들을 정리. 127 보다 작으면 검은색, 127보다 크면 흰색
for i in range(len(photoAry)):
    if photoAry[i] <= 127:
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