def solution(dic1):
    List = []
    for k, v in dic1.items() :
        a = (k,v)
        List.append(a)
    return List


dict_available = {1: 10, 2: 20, 3: 30, 4: 40}

solution(dict_available)
