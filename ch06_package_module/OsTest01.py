import os

# save_path = input('생성할 폴더 이름 입력 : ')
#
# boolean = (os.path.isdir(save_path))
# if not boolean:
#     os.mkdir(save_path)
#     print(f'{save_path} 폴더를 생성하였습니다.')
# else:
#     print('폴더가 존재합니다.')

# 특정 디렉토리에 하위 디렉토리 여러 개 생성하기
targetFolder = 'd:\\' # \는 특수 문자라서 \\라고 표시해야 합니다.
parentPath = os.path.join(targetFolder, 'sample')
print(parentPath)

try:
    os.mkdir(parentPath)
    # 반복문을 사용하여 하위폴더 10개를 만들어봅니다.
    for idx in range(1, 11):
        newFolder = os.path.join(parentPath,str(idx).zfill(4))
        print(newFolder)
        os.mkdir(newFolder)
except FileExistsError:
    print('해당 디렉토리가 이미 존재합니다.')














