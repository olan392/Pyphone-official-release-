from sys import exit
from os import system as more
from time import sleep
apps_pyp = ['dotly', 'vhi']
apps_installed = []

def home():
    more('clear')
    print('welcome to the new pyphone 1.1.0 the official release')
    print('0. exit')
    print('1. calc')
    print('2. notes')
    print('3. PYP terminal')
    print('4. PYP store')
    print('5. PYP opener')
    app_open = input('app: ')
    try:
        if int(app_open) == 1:
            calc()
        elif int(app_open) == 2:
            notes()
        elif int(app_open) == 0:
            exit()
        elif int(app_open) == 3:
            PYP_terminal()
        elif int(app_open) == 4:
            PYP_store()
        elif int(app_open) == 5:
            PYP_opener()
    except Exception:
        print('not valid')
        sleep(2)
def calc():
    more('clear')
    print('add exit to exit')
    print('operators: +, -, *, /, **, //, %')
    try:
        print('exitapp to exit')
        expr = input("Enter calculation: ")
        if expr == 'exitapp':
            return
        result = eval(expr)
        print(f'Result: {result}')
        sleep(2)
    except:
        print('invalid input')
        sleep(1)
        home()
def notes():
    more('clear')
    print('exitapp to exit')
    note = input('note: ')
    if note == 'exitapp':
        return
    print(note)
    sleep(2)
def PYP_terminal():
    more('clear')
    print('use exit to exit')
    while True:
        cmd = input('>> ')
        if cmd == 'pyp say':
            say = input('say:  ')
            print(say)
        elif cmd == 'exit':
            break
        elif cmd == 'clear':
            more('clear')
        elif cmd == 'pyp help':
            print('commands: pyp say, exit, clear, pyp help')
        else:
            print('not a command use pyp help')
def dotly():
    more('clear')
    print('.')
    sleep(1)
    more('clear')
    print('..')
    sleep(1)
    more('clear')
    print('...')
    sleep(1)
    return
def PYP_store():
    global apps_pyp, apps_installed
    while True:
        more('clear')
        print('welcome to pyp store exitapp to exit')
        print('availiable apps:', *apps_pyp)
        print('installed apps:', *apps_installed)
        app_pyp = input('app:  ')
        if app_pyp == 'dotly':
            apps_pyp.remove('dotly')
            apps_installed.append('dotly')
        elif app_pyp == 'vhi':
            apps_pyp.remove('vhi')
            apps_installed.append('vhi')
        elif app_pyp == 'exitapp':
            break
def PYP_opener():
    more('clear')
    print('welcome to PYP opener exitapp to exit')
    print('installed apps:', *apps_installed)
    while True:
        app_opener = input('app:  ')
        if 'dotly' in apps_installed:
            if app_opener == 'dotly':
                dotly()
                break
        if 'vhi' in apps_installed:
            if app_opener == 'vhi':
                vhi()
                break
        if app_opener == 'exitapp':
            break
        else:
            print(f'{app_opener} not installed')
def vhi():
    more('clear')
    sleep(1)
    print('.')
    sleep(1)
    more('clear')
    print('..')
    sleep(1)
    more('clear')
    print('...')
    sleep(1)
    more('clear')
    print('welcome to vhi exitapp to exit better than you notes app!')
    while True:
        vhin = input('note:  ')
        if vhin == 'exitapp':
            break
        print(vhin)
def loading():
        more('clear')
        sleep(1)
        print('.')
        sleep(1)
        more('clear')
        print('..')
        sleep(1)
        more('clear')
        print('...')
        sleep(1)
        more('clear')
        more('clear')
        sleep(1)
        print('.')
        sleep(1)
        more('clear')
        print('..')
        sleep(1)
        more('clear')
        print('...')
        sleep(1)
        more('clear')
loading()
while True:
    home()