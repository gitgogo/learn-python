#coding=utf-8
def handle_money(money):
    money_int=str(money).split('.')[0][::-1]
    result=''
    for index in range(len(money_int)):
        if not index%3:
            result+=money_int[index:index+3]+','
    return result.strip(',')[::-1]

print handle_money(5674832648)