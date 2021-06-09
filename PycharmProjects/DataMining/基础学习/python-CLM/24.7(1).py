list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# def func1(x,y):
#     x = x*2
#     y = y*2
#     return x,y


print(list(map(lambda x, y: str(x) + y, list1, list2)))



