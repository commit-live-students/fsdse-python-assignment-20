def solution(dic1):
    tup = ()
    list_of_tuples = []
    for k,v in dic1.iteritems():
        list_of_tuples.append((k,v))
    return list_of_tuples

dic = {1: 10, 2: 20, 3: 30, 4: 40}
print solution(dic)
