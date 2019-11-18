# -*- coding: utf-8 -*-
import re


# 处理列表，计算文字个数
def check_contain(file_path):
    word_count_num = {}
    word_file = open(file_path, 'r', encoding='utf-8-sig')
    word = word_file.read()
    word_file.close()

    # 暂时仅用文本的第一个字判断文本是中文文本还是英文文本
    if u'\u4e00' <= word[0] <= u'\u9fff':
        word_list = operation_ch_file(word)
    else:
        word_list = operation_en_file(word)

    # 统计列表里的每个字的字数返回字典
    for w in word_list:
        if w in word_count_num:
            word_count_num[w] = word_count_num[w] + 1
        else:
            word_count_num[w] = 1

    return word_count_num


# 处理中文文本，返回所有文字为一个列表
def operation_ch_file(word):
    word_2 = re.sub('[，~。、\n^a-zA-Z,:{}！@￥%+—*&“”]', '', word)     # 去掉特殊字符
    word_3 = word_2.replace(" ", "")                           # 去掉空格
    word_ch_list = (",".join(word_3)).split(',')             # 处理成列表
    return word_ch_list


# 处理英文文本，返回所有文字为一个列表
def operation_en_file(word):
    word_2 = re.sub('[~.,@#$%^&*\n:{}!@￥%+—*&、）(<>\']', ' ', word)  # 处理特殊字符
    word_en_list = word_2.split()                  # 处理空格
    return word_en_list


# 将字典写入文档
def write_file(content):
    content_file = open('word_num_counter.txt', 'w')
    # 将字典按value大小，从大到小排序，并且写入文件
    for k in sorted(content, key=content.__getitem__, reverse=True):
        content_s = k + " ： " + str(content[k]) + "\n"
        content_file.write(content_s)
    content_file.close()


if __name__ == '__main__':
    write_file(check_contain(input('请输入文件路径：')))
