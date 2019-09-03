#ex_1
def create(n):
    import os
    
    path = os.getcwd()
    for i in range(1,(n+1)):
        direct = r'{0}\dir_{1}'.format(path,i)
        try:
            os.mkdir(direct)
        except FileExistsError:
            continue
            




        
def delete(n):
    import os
    
    path = os.getcwd()
    for i in range(1,(n+1)):
        direct = r'{0}\dir_{1}'.format(path,i)
        try:
            os.rmdir(direct)
        except FileNotFoundError:
           continue
#ex_2
def tree():
    import os
    tree = os.walk(os.getcwd())
    dirs = []

    for cort in tree:
        dirs = cort [1]
        break
    return dirs

#ex_3

def copy():
    
    import sys 
    import shutil 
    import os
    
    tree = os.walk(os.getcwd())
    files = []

    for cort in tree:
        name = cort [2][0]
        break

    file = sys.argv[0]

    copy = r'{0}\{1}_copy.py'.format(os.getcwd(),name[0:(len(name)-3)])

    shutil.copyfile(file,copy)

    

        
