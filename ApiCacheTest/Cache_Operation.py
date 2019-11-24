# -*- coding: utf-8 -*-
from datetime import datetime as d


# 用于写入缓存文件
class CacheOperation:
    def __init__(self, http_content):
        self.http_content = http_content

    def operation_file(self):

        cache_path = "./cache/" + "{}-{}-{}.txt".format(d.now().year, d.now().month, d.now().day)
        content_file = open(cache_path, 'w', encoding='utf-8-sig')
        content_file.write(self.http_content)
        content_file.close()

