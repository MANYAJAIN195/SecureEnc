
def encrypt(text: str, shift: int):
    text=text.replace(" ", "")
    encrypted = ""
    if isinstance(shift, int):
        for i in text.upper():
            if(ord(i) + shift)>91:
                encrypted += chr(ord(i) + shift-91+65)
            else:
                encrypted += chr(ord(i) + shift)
        return encrypted
    


def decrypt(text: str,shift: int):
    text=text.replace(" ", "")
    decrypted = ""
    for char in text.upper():
        if(ord(char) - shift)<65:
            decrypted += chr(ord(char) - shift+90-65+1)
        else:
            decrypted += chr(ord(char) - shift)
    return decrypted
