order0 = '''abcdefghijklmnopqrstuvwxyz'''
order1 = '''d8x3a'p?yw;k6q-ue:g2.v#9$5t,lz7i"!1 o04rbfshmjc'''
ciphers=[order0,order1]
cipher=1
key = 2

def encrypt(str):
    str_encrypted =''
    str = str.lower()
    for letter in (str):
        if ciphers[cipher].count(letter) !=1:
            new_letter = ''
        else:
            new_letter = ciphers[cipher][(ciphers[cipher].find(letter)+key)%len(ciphers[cipher])]
        str_encrypted += new_letter
    return str_encrypted

def decrypt(str):
    str_decrypted =''
    str = str.lower()
    for letter in (str):
        if ciphers[cipher].count(letter) !=1:
            new_letter = ' '
        else:
            new_letter = ciphers[cipher][(ciphers[cipher].find(letter)-key)%len(ciphers[cipher])]
        str_decrypted += new_letter
    return str_decrypted

enjoying_myself = True
badTries = 0
while enjoying_myself:
    mode = input('encrypt/decrypt?\n>>>')
    if mode == 'encrypt'or mode =='e':
        stringToEncrypt = input('secret message:\n>>>')
        key = int(input('key:\n>>>'))
        print(encrypt(stringToEncrypt))
    if mode == 'decrypt'or mode =='d':
        attempt = input("What's the password?\n>>>")
        if attempt == '************':
            print("Access Approved!")
            key = int(input('key:\n>>>'))
            stringToDecrypt = input("Enter encrypted string:\n>>>")
            print(decrypt(stringToDecrypt))
        else:
            if badTries <=4:
                badTries +=1
                print(f"Access Denied.\nReason: Incorrect Password. \n{5-badTries} attempts remaining.")
            else:
                print("Too many incorrect attempts! shutting down system...")
                break
    if mode == 'quit'or mode == 'q':
        break
    if mode == 'change cipher'or mode == 'c':
        cipher=int(input('Which cipher to use? \nrotation[0] or scrambled[1]\n>>>'))
