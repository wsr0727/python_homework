import random

# 是否无限次
guess_type = input('是否选择无限次（是或者否）:')

# 随机生成一个数字
lucky_num = random.randint(0, 1000)

# 处理是否无限次
if guess_type == "是":
    guess_num = 1
    guess_t = 0
elif guess_type == "否":
    guess_num = eval(input('你想猜几次：'))
    guess_t = 1
else:
    print('输入格式错误')

# 获取用户第一次输入
guess_what = eval(input('给我个0~1000的数字：'))
guess_count = 1
guess_show = 0
while guess_what != lucky_num:
    guess_count = guess_count + guess_t
    guess_show += 1
    if guess_count <= guess_num:
        if guess_what > lucky_num:
            guess_what = eval(input('你的数字大了，已经猜了{}次。\n重新给我个数字：'.format(guess_show)))
        elif guess_what < lucky_num:
            guess_what = eval(input('你的数字小了。已经猜了{}次\n重新给我个数字：'.format(guess_show)))
        else:
            print('没次数啦！正确数字是：', lucky_num)
    else:
        print('没次数啦')
        break
else:
    print('猜对啦！')


