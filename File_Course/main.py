from File_Course import File_Operation

if __name__ == '__main__':
    try:
        x = File_Operation.FileOperation(input('请输入文件路径：'))
        x.file_sort()
    except FileExistsError:
        print('已存在该文件')
