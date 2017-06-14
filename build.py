def solution(dic1):
    l=[]
    for x,y in dic1.items():
        l.append((x,y))
    return l
print (solution({1: 10, 2: 20, 3: 30, 4: 40}))
