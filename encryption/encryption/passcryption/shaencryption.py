
def shaencryption(new_pass):
    import uuid
    import hashlib
    from simplecrypt import encrypt, decrypt
    import binascii


    # new_pass = input('Please enter a password: ')

    salt = uuid.uuid4().hex

    hash_pass = hashlib.sha256(new_pass.encode()).hexdigest()

    # hash_password=hash_pass.append(salt)
    hash_password = hash_pass + salt
    print(hash_password)
    message = hash_password
    ciphercode = encrypt('AIM', message)
    print(ciphercode)

    hex_code = binascii.b2a_hex(ciphercode)
    scale = 16

    # Printing initial string
    print("Initial string", hex_code)

    # Code to convert hex to binary
    res = bin(int(hex_code, scale)).zfill(8)
    res=str(res)
    # Print the resultant string
    print("Resultant string", res)

    return res
