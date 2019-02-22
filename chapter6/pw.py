#! python3

# pw.py - An insecure password locker program.

PASSWORDS = {'email':   'password123',
            'blog':     'Vm4cfjkjnjJNjN$JNct5j',
            'luggage':  'UHF*73h&*H9&Fdef54h'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [Account] - copy account password')
    sys.exit()
    
account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)
