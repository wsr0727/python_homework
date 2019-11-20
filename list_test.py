# 获取用户输入
user_input = input('输入列表里的元素，仅限数字，以空格隔开:')

# 处理用户输入,将用户输入的字符串转换为数字列表
user_list = user_input.split()
L = list(map(eval, user_list))

# 取最大值
list_max = L[0]
for i in range(len(L)):
    if L[i] > list_max:
        list_max = L[i]
print('你输入的列表最大值为：', list_max)

# 取最小值
list_min = L[0]
for y in range(len(L)):
    if L[y] < list_min:
        list_min = L[y]
print('你输入的列表最小值：', list_min)

# 求平均数
list_sum = 0
for x in range(len(L)):
    list_sum = list_sum + L[x]
print('你输入的列表平均数为：', list_sum/len(L))
