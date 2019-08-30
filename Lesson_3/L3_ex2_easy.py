def paradise(tick):
    tak = []
    num = [1,2,3,4,5,6]
    for i in num:
        for_l = tick % 10
        tick = tick // 10
        tak.append(for_l)
        
    tick1 = tak[0:3]
    tick2 = tak[3:6]
    if sum(tick1) == sum(tick2):
        a = "Yes!"
    else:
        a = "Sorry,nope!"
    return a
