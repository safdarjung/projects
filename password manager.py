from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key','wb') as key_file:
#         key_file.write(key)
# write_key()

def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data =line.rstrip()
            user,psswrd = data.split('|')
            print(f"USER ={user} PASSWORD = {str(fer.decrypt(psswrd.encode()).decode())}")


def add():
    name = input('acc name: ')
    pwd = input('password: ')

    with open('passwords.txt','a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode()).decode()) +'\n')


key = load_key()
fer = Fernet(key)

while True:
    mode = input('add new psswrd/view existing psswrds[view/add], press q to quit ').lower()
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('invalid mode')