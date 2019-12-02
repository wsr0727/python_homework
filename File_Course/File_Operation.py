# -*- coding: utf-8 -*-
import os


# 用于写入缓存文件
class FileOperation:
    def __init__(self, file_dir):
        self.file_dir = file_dir

    def file_sort(self):
       # 获取文件创建时间
       for root, dirs, files in os.walk(self.file_dir):
           for f in files:
               old_name = os.path.join(root, f)
               time = os.path.getctime(old_name)
               print(time)
    def file_rename(self):

        for root, dirs, files in os.walk(self.file_dir):
            num = 1
            for f in files:

                old_name = os.path.join(root, f)
                new_name = os.path.join(root, str(num)+f)
                os.rename(old_name, new_name)
                num += 1
