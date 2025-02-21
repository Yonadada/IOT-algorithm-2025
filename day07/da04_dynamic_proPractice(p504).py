# da04_dynamic_proPractice(p504).py

## == 황금미로 == ##
import random

황금미로 = []

for _ in range(5):
    gRow = []
    
# 리스트의 첫번째 값은 0이 안나오게
    value = random.randint(1,5)
    gRow.append(value)
    
# 1번째부터 마지막까지 0제외한 숫자
    gRow.extend([random.randint(0,5) for _ in range(4)])
    황금미로.append(gRow)

#출력
for row in 황금미로:
    print(gRow)

메모이제이션 = [[0 for _ in range(5)] for _ in range(5)]

#황금미로 값으로 메모이제이션 값 채움
rowHap = gRow[0][0]


