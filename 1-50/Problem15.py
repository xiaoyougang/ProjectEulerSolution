def combination(total, selection):
    if (total - selection) < selection:
        selection = total - selection
    r1 = 1
    r2 = 1
    for i in range(0,selection):
        r1 = r1 * (total - i)
        r2 = r2 * (i + 1)
    return r1 / r2
print combination(4, 2)
print combination(6, 3)
print combination(8, 4)
print combination(40, 20)
