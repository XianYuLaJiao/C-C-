def print_food(*food, place, waiter):#括号内包括可变参数和两个一般参数，所以在实际调用的时候要区分开来，一般参数要用关键字参数调用
    print('这是第' + place + '卓的客人点的菜单：')
    for f in food:
        print(f, end=' ')
    print('\n服务员：' + waiter)


# print_food('宫保鸡丁', '梅菜扣肉', '牛杂', '5', '小李')
# 结果：#TypeError: print_food() missing 2 required keyword-only arguments: 'place' and 'waiter'
# 参数*food, place, waiter 是三个参数，*food为可变参数， place，water是形式参数，
# 在输入调用时必须和*food区分开来，所以调用时必须用关键字参数才可以，并且记住关键字参数应该写在后边所以
print_food('宫保鸡丁', '梅菜扣肉', '牛杂', place='5', waiter='小李')
#结果：这是第5卓的客人点的菜单：
# 宫保鸡丁 梅菜扣肉 牛杂
# 服务员：小李
