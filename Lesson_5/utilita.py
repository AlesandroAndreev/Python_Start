def utilita():
    print ('way - перемещение между папками.')
    print('create - команда на создание папки')
    print ('delete - команда на удаление папки')
    print('exit - выход')

    

    while True:
        import Modul.easy as ex

        
        print(ex.tree())

        print('Введите команду!')
        print ('way(name,reverse=False) - перемещение между папками. Если перемещение оскществляется обратно, вместе с именем предается команда reverse = True')
        print('create(name) - команда на создание папки')
        print ('delete() - команда на удаление папки')
        print('exit - выход')

        command = input()

        if command == 'create':
            name = input('Введите имя файла: ')
            ex.create(name)
            continue
        elif command =='delete':
            name = input('Введите имя файла: ')
            ex.delete(name)
            continue
        elif command =='way':
            name = input('Введите имя файла: ')
            ret = input('up or down: ')
            if ret == 'up':
                ex.way(name)
                continue
            elif ret == 'down':
                ex.way(name,reverse = True)
                continue
            else:
                print('Такой команды нет, попробуйте еще раз!')
                continue
        elif command == 'exit':
            break
        else:
            print('Такой команды нет, попробуйте еще раз!')
            continue
        
            

        



    
           
        
