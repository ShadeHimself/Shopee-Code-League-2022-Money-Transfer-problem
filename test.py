def sum_up(*args):
    s = 0
    for i in args:
        s += i
    
    print(s)
    return s

sum_up(2, 2, 2)