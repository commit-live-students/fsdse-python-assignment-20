
def solution(dic1):
    '''To get the dictionary by iterating up from list'''
    dicList = []
    for k,v in dic1.items():
        dicist = dicList.append((k,v))
    print dicList    
    return dicList

solution({1: 10, 2: 20, 3: 30, 4: 40})
