# 获取月薪收入
income = eval(input('请输入工资;'))
tax = 0

# 判断月薪所属个税层级
if 0 < income <= 3500:
    print('你真是太穷了，不用交税')
elif 3500 < income <= 83500:
    if income - 3500 <= 1500:
        tax = (income - 3500) * 0.03
    elif 1500 < income - 3500 <= 4500:
        tax = (income - 3500) * 0.1
    elif 4500 < income - 3500 <= 9000:
        tax = (income - 3500) * 0.2
    elif 9000 < income - 3500 <= 35000:
        tax = (income - 3500) * 0.25
    elif 35000 < income - 3500 <= 55000:
        tax = (income - 3500) * 0.30
    elif 55000 < income - 3500 <= 80000:
        tax = (income - 3500) * 0.45
    print('你需要交{:.2f}税，剩余{:.2f}元'.format(tax, income - tax))
elif 83500 < income:
    print('你真是太富有了')
else:
    print('你的工资不真实，重新输入')


