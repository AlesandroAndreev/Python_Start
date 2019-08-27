def phil (fun,vec):
    if fun == None:
        for i in vec:
            if (i == False) or (i == ''):
                vec.remove(i)
    else:
        for i in vec:
            if (fun(i) == False) or (fun(i) == ''):
                vec.remove(i)
    return vec

        
    
