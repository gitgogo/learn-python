#coding=utf-8
'''
随机生成一个数，然后限定猜5次，猜大了提示猜大了，猜小了提示猜小了，
如果相等，则提示中大奖，并退出循环。
如果5次没猜对，那么就提示没机会了，并且公布正确答案

1 生成随机整数（有一定的范围），存到一个变量里面
2 循环5次并控制循环退出条件
3 每次循环中读入一个整数。（raw_input,必须要int转类型）:输入类型的判断，是否是整数或者小数
4 比较的3种：大于（提示：大了，第五次的时候打印随机数）、小于（小了，第五次的时候打印随机数）和等于（猜中了，break）
5 打印一句话，执行完毕：print done
'''
import random
guess_number=random.randint(0,99)
loop_times=0
while loop_times<5:
    try:
        user_input_number=int(raw_input('请输入一个随机整数，范围 0-99: '.decode('utf-8').encode ('gbk')))
    except Exception ,e:
        print u'请输入数字： '#捕获异常继续执行程序，continue下一次循环
        continue
    if user_input_number<guess_number:
        print u'您猜的数字小于答案'
        if loop_times==5:
            print u'没有机会了！正确数字是: '+str(guess_number)
    elif user_input_number>guess_number:
        print u'您猜的数字大于答案'
        if loop_times==5:
            print u'没有机会了！正确数字是: '+str(guess_number)
    elif user_input_number==guess_number:
        print u'恭喜您猜中了'
        break
    loop_times+=1
    if loop_times==5:
        print u'没有机会了！正确数字是: '+str(guess_number)
