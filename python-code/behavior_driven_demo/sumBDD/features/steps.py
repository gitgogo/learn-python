def sum(a,b):
    return a+b

@step('I have the numbers (\d+),(\d+)')
def have_the_number(step, number1,number2):
    # 将通过正则表达式匹配的数字存于全局变量world中
    world.number1 = int(number1)
    world.number2 = int(number2)

@step('I compute its sum')
def compute_its_sum(step):
    # 从全局变量world中取出匹配的数字，
    # 计算其阶乘，并将结果再存回world中
    world.sum = sum(world.number1,world.number2)

@step('I see the number (\d+)')
def check_number(step, expected):
    # 通过正则匹配到预期数字
    expected = int(expected)
    expected = int

2017-06-03 11:39:58  吴老师(875821166)
(expected)
    # 断言计算阶乘结果是否等于预期
    assert  world.sum == expected, "Got %d" %world.sum