# -*- coding: utf-8 -*-
import os


# 用于写入缓存文件
class FileOperation:
    def __init__(self, file_dir):
        self.file_dir = file_dir

    def file_rename(self):
        '''
        将文件统一增加前缀
        :return: file_new_name 修改前缀后的文件名以列表形式
        '''
        file_new_name = []
        for root, dirs, files in os.walk(self.file_dir):
            for f in files:
                file_path = os.path.join(root, f)
                new_name = os.path.join(root, 'wsr' + f)
                os.rename(file_path, new_name)
                file_new_name.append(new_name)
        return file_new_name

    def file_sort(self):
        '''
        获取文件创建时间，按时间加入编号，并按时间排序输出新文件名
        :return: None
        '''
        num = 1
        file_sort_dict = {}
        for f in self.file_rename():
            file_sort_dict[f] = os.path.getctime(f)

        for k in sorted(file_sort_dict, key=file_sort_dict.__getitem__):
            name, suffix = os.path.splitext(k)
            name_num_path = name + str(num) + suffix
            file_new_path, file_new_name = os.path.split(name_num_path)
            os.rename(k, name_num_path)
            print(file_new_name)
            num += 1

