
def example (ruls = False):
    
    import random

    example = []

    if ruls == True:
        start = int(input('Введите левый предел:  '))
        finish = int(input('Введите правый предел:  '))
        count = int(input('Введите количество символов:  '))
    elif ruls == False:
        start = 0
        finish = 30
        count = 20

    for i in range(count):
        example.append(random.randint(start,finish))
        continue
    
    return example

def fruits():

    import random

    fru  = ['Груша', 'Киви', 'Банан', 'Яблоко', 'Абрикос', 'Апельсин', 'Ананас', 'Черешня' , 'Лимон']

    r_fru = [random.choice(fru) for i in range(len(fru))]

    return r_fru
     
    

# ex_1 ( lists можно изменить на example() )
def kvadrat (lists):
    result = [i**2 for i in lists]
    return result

# ex_2 ( lists можно изменить на fruits() )
def sort_fruits(fru_1, fru_2):
    sort = [i for i in fru_1 if i not in fru_2]
    return sort


#ex_3 ( lists можно изменить на example() )  
def sort (lists):
    result = [i for i in lists if (i>0 and i%3 == 0 and i % 4 !=0)]
    return result
