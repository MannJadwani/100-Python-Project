while True:
    master_pwd = input("What is the master password? ")

    saved_pwd='SubscribeToMannJadwani'


    if master_pwd == saved_pwd:

        while True:
            mode = input('would you like to view your passwords or add a password(view,add)?')

            def view():


                with open('password.txt','r') as f:
                    for line in f.readlines():
                        print(line)

            def add():
                platform = input('Platform:')
                name=input('Account Name: ')
                pwd = input('Password: ')

                with open('password.txt','a') as f:
                    f.write(platform +'|'+ name +'|'+ pwd+ '\n')

            if mode == 'q':
                quit()
            if mode=='view':
                view()
            elif mode == 'add':
                add()
            else:
                print('invalid input')
            continue
    else:
        print('Wrong Password')
        continue

