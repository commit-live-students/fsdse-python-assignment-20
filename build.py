def solution(dic1):
    l=list()
    for k,v in dic1.items():
        l.append((k,v))
    return l

d={1: 10, 2: 20, 3: 30, 4: 40}
print(solution(d))
