import os
from File_Course import File_Operation
if __name__ == '__main__':
    try:
        # os.mkdir('./1')
        # content_file = open('./1/123.txt', 'w', encoding='utf-8-sig')
        # content_file = open('./1/124.txt', 'w', encoding='utf-8-sig')
        x = File_Operation.FileOperation('./1')
        x.file_rename()
        x.file_sort()
    except FileExistsError:
        print('已存在该文件')