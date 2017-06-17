def solution(dic1):
    '''Enter code here'''
    lst = []
    for i in dic1.items():
        lst.append(i)
    return lst

d1 = {1: 10, 2: 20, 3: 30, 4: 40}
print(solution(d1))
