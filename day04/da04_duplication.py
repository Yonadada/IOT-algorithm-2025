#da04_duplication.py

# 응용예제 - 폴더 및 하위 폴더에 중복된 파일 이름 찾기
# pg 311 
import os


class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
    

# 전역변수 선언 
memory = []
root = None
fnameAry = []

# 메인코드
if __name__ == '__main__':
    
    folderName = 'C:/Program Files/common Files/'
    for dirName, subDirList, fnames in os.walk(folderName):
        for fname in fnames:
            fnameAry.append(fname) # 파일면 추가
            

    node = TreeNode()
    node.data = fnameAry[0]
    root = node
    memory.append(node)
        
    dupNameAry = []
        
    for name in fnameAry[1:]:
        node = TreeNode()
        node.data = name
        
        current = root
        while True:
            if name == current.data:
                dupNameAry.append(name)
                break
            
            if name < current.data:
                if current.left == None:
                    current.left = node
                    memory.append(node)
                    break
                current = current.left
            
            else:
                if current.right == None:
                    current.right = node
                    memory.append(node)
                    break
                current = current.right
                
    dupNameAry = list(set(dupNameAry))
    # dupCounts ={}

    
    print(f'{folderName} 및 그 하위 디렉터리의 중복된 파일 목록 --> ')
    print(dupNameAry)
        