

def encrypt(key,text):
    plain_text = text.strip()
    key = key.strip()
    key = key.upper()
    cipher_text=[]
    for i in plain_text.upper() :
        if(i < 'A' or i> 'Z'):
            cipher_text.append(i)
            continue
        cipher_text.append(key[ord(i) - ord('A')])
    return "".join(cipher_text)



def decrypt(key,text):
    cipher_text = text.strip()
    key = key.strip()
    key = key.upper()
    plain_text = []
    for i in cipher_text :
        if(i < 'A' or i> 'Z'):
            plain_text.append(i)
            continue
        plain_text.append(chr(ord('A') + key.index(i)))
        
    return "".join(plain_text)

def isUniqueChars(st):
    char_set = [False] * 128
    for i in range(0, len(st)):
        val = ord(st[i])
        if char_set[val]:
            return False
 
        char_set[val] = True
 
    return True