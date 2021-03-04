from simplecrypt import decrypt
import binascii
import hashlib

def decrypt_new(pass_old):
    decimal_representation = int(pass_old,2)
    hexadecimal_string = hex(decimal_representation)

    print(hexadecimal_string)
    hex_byte, a = hexadecimal_string.split('0x')
    # print(hex_byte)
    print(a)
    hex_byte = bytes(a, 'utf-8')

    print(hex_byte)
    hex_byte = binascii.a2b_hex(hex_byte)
    print(hex_byte)
    original = decrypt('AIM', hex_byte)
    print(original)
    hash_p = original[0:64]

    password = str(hash_p, 'UTF-8')
    print(password)
    return password


def convert_password(user_password):
    # password, salt = hashed_password.split(':')
    # print(password)
    new = hashlib.sha256(user_password.encode()).hexdigest()
    print(new)
    return new












