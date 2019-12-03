import os
import time


def simple_dir(file_dir):
    """
    显示路径下所有文件或文件夹的信息
    :param file_dir: 文件路径
    :return:
    """
    file_num = 0
    dir_num = 0
    file_size = 0
    for f in os.listdir(file_dir):
        file_path = os.path.join(file_dir, f)
        time_local = time.localtime(os.path.getctime(file_path))
        file_time = time.strftime("%Y/%m/%d  %a %H:%M:%S", time_local)
        if os.path.isdir(file_path) is True:
            file_isdir = '<DIR>'
            dir_num += 1
        else:
            file_isdir = os.path.getsize(file_path)
            file_size = file_size + file_isdir
            file_num += 1
        print(file_time, file_isdir, f)
    print(file_num, '个文件   ', file_size, '字节')
    print(dir_num, '个目录')


if __name__ == '__main__':
    simple_dir(input("文件路径："))
