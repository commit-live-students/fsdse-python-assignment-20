def solution(dic1):
    y = []
    for k,v in dic1.iteritems():
        y.append((k,v))
    return y

print solution({4:40,1:10,2:20,3:30})
