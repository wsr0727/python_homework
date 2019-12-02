# -*- coding: utf-8 -*-
import os


# 用于写入缓存文件
class FileOperation:
    def __init__(self, file_dir):
        self.file_dir = file_dir

    def file_rename(self):
        file_new_name=[]
        for root, dirs, files in os.walk(self.file_dir):
            for f in files:
                file_path = os.path.join(root, f)
                new_name = os.path.join(root, 'wsr' + f)
                os.rename(file_path, new_name)
                file_new_name.append(new_name)
        return file_new_name
    def file_sort(self):
        # 获取文件创建时间,并写入字典
        file_sort = {}
        for f in self.file_rename():
            file_sort[f] = os.path.getctime(f)

        for k in sorted(file_sort, key=file_sort.__getitem__):
            return k

    def file_rename2(self):
        #从后往前数 第一个小数点前加序号

        for root, dirs, files in os.walk(self.file_dir):
            num = 1
            for f in files:
                file_path = os.path.join(root, f)
                new_name = os.path.join(root, str(num) + f)
                os.rename(file_path, new_name)
                num += 1


x = FileOperation('./1')
print(x.file_sort())
