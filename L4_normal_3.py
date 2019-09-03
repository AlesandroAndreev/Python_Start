

def ex3_norm():
    import random
    import os
    

    text = [random.randint(0,9) for i in range(2500)]
    path = '{0}\\ex3.txt'.format(os.getcwd())
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(str(text))


def ex3_norm1():
    import os
    import itertools
    
    _=[]
    
    path = '{0}\\ex3.txt'.format(os.getcwd())
    
    with open(path, 'r', encoding='UTF-8') as file:
        stroka_1 = list(file.read())
    for i in stroka_1:
        if i not in ['[',',',']',' ']:
            _.append(int(i))
            
    stroka_2 =  max((list(g) for k, g in itertools.groupby(_)), key=len)
    return stroka_2

