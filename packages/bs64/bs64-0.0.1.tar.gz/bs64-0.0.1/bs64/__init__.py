def Encode(Script_Name:str,New_Script_Name:str):
    new = open(New_Script_Name,'w')
    try:
        file = open(Script_Name,'r').read()
    except FileNotFoundError:
        print('Not Found Script')
        exit()
    key = 'TC'
    iv = 'Toxic Code'
    cipher = "".join(reversed(file))
    cipher = b16encode(cipher.encode('utf-8'))
    cipher = b32encode(cipher)
    cipher = b64encode(cipher)
    cipher = dumps(cipher)
    cipher = compress(cipher)
    crypt = AES.new(b'\x9bm\x9a\xef\x1f3&\x0c\xb2\xc7\xbd\x8e\xc7>\xb9\x04',AES.MODE_OFB,b'\xabw\x95\x17\xbav\xf1\x94tru<\xf29\xc7j')
    cipher = crypt.encrypt(cipher)
    cipher = b16encode(cipher)
    new.write(f'''from ccode import *
Run('{cipher.decode('utf-8')}')''')
    new.close()
if __name__ != '__main__':
    from base64 import *
    from marshal import dumps,loads
    from zlib import compress,decompress
    from Crypto.Cipher import AES
