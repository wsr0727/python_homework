import random

# 获取输入次数
guess_num = eval(input('你想猜几次：'))

# 随机生成一个数字
lucky_num = random.randint(0, 1000)

# 获取用户第一次输入
guess_what = eval(input('给我个0~1000的数字：'))
guess_num = guess_num - 1
while guess_what != lucky_num:
    while guess_num > 0:
        guess_num = guess_num - 1
        if guess_what > lucky_num:
            guess_what = eval(input('你的数字大了，还有{}次机会。\n重新给我个数字：'.format(guess_num)))
        else:
            guess_what = eval(input('你的数字小了。还有{}次机会\n重新给我个数字：'.format(guess_num)))
    else:
        print('没次数啦！正确数字是：', lucky_num)
        break

else:
    print('猜对啦！')
