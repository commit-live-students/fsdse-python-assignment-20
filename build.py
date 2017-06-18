def solution(dic1):
    '''Enter code here'''
    l = []
    for x,y in dic1.items():
        l.append((x,y))
    return sorted(l)
