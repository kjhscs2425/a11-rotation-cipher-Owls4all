import string

alphabet = string.ascii_lowercase
print(alphabet)

password = "hi potato zzz"
# eve wants to steal my password

# make my password secret
key = 16

def encrypt(plaintext):
    ciphertext = ""
    for letter in plaintext:
        old_position = alphabet.find(letter)
        if old_position == -1:
            ciphertext += " "
        else:
            new_position = old_position + key
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            ciphertext += new_letter
    return ciphertext

print(encrypt(password))

# Your task:
# figure out what key I used to encrypt this message:
secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"
secret_message_decrypted = 'i am a secret message you will never guess'
#Athena says: Now try to decrypt mine:
my_challenge = '''"x#j#fu011f's3#f;f"03#fux#f0f$jsuf"0j#pfsdfuj0"0$f'sp#f"sf6j0"fsv"fs8#8#!fcv"f0"f08fs"f"sp;-t'''
#Yes, there are supposed to be quotes in it. And special characters. Good luck!