def way (name,revers = False):
    import os
    if revers == True:
        way = r'{0}'.format(os.getcwd()[0:os.getcwd().find(str(name))+len(str(name))])
    else:
        way = r'{0}\{1}'.format(os.getcwd(),str(name))
    try:
       os.chdir(way)
       print ("Успешно перешел")
    except FileNotFoundError:
        print ("Невозможно перейти")
    
def create (name):
    import os
    way = r'{0}\{1}'.format(os.getcwd(),str(name))
    try:
        os.mkdir(way)
        print ("Файл создан")
    except FileExistsError:
        print ("Невозможно создать")

def delete (name):
    import os

    way = r'{0}\{1}'.format(os.getcwd(),str(name))
    try:
        os.rmdir(way)
        print ("Успешно удалил")
    except FileNotFoundError:
        print ("Невозможно удалить")

def ls():
    import os
    print (os.getcwd())
