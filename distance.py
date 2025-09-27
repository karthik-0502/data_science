
def fun_dist(x1,y1,x2,y2):
    dx = (x2-x1)**2
    dy = (y2-y1)**2
    result = (dx + dy)**0.5
    return result

def fun_man(x1,y1,x2,y2):
    if x1 >= x2:
        dx = x1-x2
    else:
        dx = x2-x1
    if y1 >= y2:
        dy = y1-y2
    else:
        dy = y2-y1
    result = dx + dy
    return result