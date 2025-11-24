import os

targetFolder = 'd:\\'
folderName = ['alpha', 'bravo','delta','terra','pixel','orbit','matrix','spark','fusion']
parentPath = os.path.join(targetFolder, 'exercise')

try:
    os.mkdir(parentPath)
    # 반복문을 사용하여 하위폴더 10개를 만들어봅니다.
    for name in folderName:
        newFolder = os.path.join(parentPath,str(name))
        print(newFolder)
        os.mkdir(newFolder)
except FileExistsError:
    print('해당 디렉토리가 이미 존재합니다.')