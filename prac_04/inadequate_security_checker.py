# Woefully inadequate security checker
# by Jan Crooks
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']

user_input = input("Please enter your username: ")
if user_input in usernames:
    print("Access Granted")

else:
    print("Access Denied")
