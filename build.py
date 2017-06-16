def solution(dic1):
    ls = []
    for e in dic1:
        ls.append((e,dic1[e]))
    return ls


solution({1:10,2:20,3:30,4:40})
