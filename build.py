def solution(dic1):

    l=[]
    pair= ()
    for key in sorted(dic1.keys()):
        pair = (key, dic1[key])
        l.append(pair)
    return l
print solution({1: 10, 2: 20, 3: 30, 4: 40})
