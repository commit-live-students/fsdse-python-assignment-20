def solution(dic1):
    '''Enter code here'''
    result =[]
    for key in dic1.keys():
        result.append((key,dic1[key]))
    return sorted(result)
