import operator

def solution(dic1):
    '''Enter code here'''
    return sorted(dic1.items(), key=operator.itemgetter(1))



a = {1: 10, 2: 20, 3: 30, 4: 40}
print solution(a)
