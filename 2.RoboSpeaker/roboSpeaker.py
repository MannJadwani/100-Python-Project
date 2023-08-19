import os 

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    x = input('Enter What You Want To say')
    command = f'say{x}'
    os.system(command)