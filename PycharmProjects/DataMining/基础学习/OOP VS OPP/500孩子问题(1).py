'''
500个孩子围成圈，逢三出圈，一直到最后一个，那么留在圈中的最后一个孩子是几号。
面向过程解决办法
'''

# cycle = list(range(1, 501))
cycle = [i for i in range(1, 501)]
step = 1
while len(cycle) > 1:
    kids = []
    for kid in cycle:
        step += 1
        if step % 3 == 0:
            kids.append(kid)

    for kid in kids:
        cycle.remove(kid)

print(cycle)

