# -*- coding: utf-8 -*-
import re
import os

class CaheOperationg:
    def __init__(self, http_content):
        #self.file_path = file_path
        self.http_content = http_content

    def operation_file(self):
        file1 = '/cache/test.txt'
        content_file = open(r"test.txt", 'w', encoding='utf-8-sig')
        content_file.write(self.http_content)
        content_file.close()
