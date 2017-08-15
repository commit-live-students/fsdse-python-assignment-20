def solution(dic1):
    '''Enter code here'''
    op = ()
    output = []
    for i in range (0,len(dic1) - 1):
        for k, v  in dic1.iteritems():
            op = (k,v)
            output.append(op)
        return output


'''
dic1 = {1: 10, 2: 20, 3: 30, 4: 40}
a = solution(dic1)
print a
'''
