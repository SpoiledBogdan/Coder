import math


def dec_to_bin():

    # validating user input
    while True:
        try:
            dec = int(input("Type a dec number: "))
            string = ''
            if isinstance(dec, bool):   # if dec is not int
                raise ValueError
        except ValueError:
            print("You should type a dec number! ")
        else:
            break

    while dec >= 1:
        bin_ = math.floor(dec % 2)
        string += str(bin_)
        dec = dec / 2

    print(string[::-1])


def bin_to_dec():
    dec = 0

    # validating user input
    while True:
        try:
            bin_int = int(input("Type a binary number: "))
            bit_list = list(str(bin_int))

            for i in list(str(bin_int)):
                if i != '1' and i != '0':
                    raise ValueError
        except ValueError:
            print("You should type a binary number! ")
        else:
            break

    size = len(bit_list)

    for i in range(size):
        if bit_list[i] == '0':
            continue
        else:
            bit_list[i] = (2 ** (size - i - 1))
            dec += bit_list[i]
    print(dec)


def xor_cipher():
    message = list(str(input("Type a message: ")))
    key = list(str(input("Type a key: ")))

    message_list = []
    key_list = []
    encode_result = []
    decode_result = []

    new_key = []

    coefficient = int(len(message) / len(key))
    modulo = len(message) % len(key)

    # filling in the key along the length of the message
    for i in range(coefficient):
        new_key += key
    for i in range(modulo):
        new_key += key[i]

    # message to dec
    for i in range(len(message)):
        message_list.append(ord(message[i]))

    # key to dec
    for i in range(len(new_key)):
        key_list.append(ord(new_key[i]))

    # encode result
    for i in range(len(message)):
        encode_result.append(int(message_list[i]) ^ int(key_list[i]))
    print("Encode message: ", encode_result)    # I have to print a list of numbers, not an array of numbers

    # decode result
    for i in range(len(encode_result)):
        decode_result.append(chr(encode_result[i] ^ key_list[i]))
    print("Decode message: ", ''.join(decode_result))


while True:
    char_input = int(input("Enter the number for the command:\n1. Dec to bin\n2. Bin to dec\n3. Xor cipher\n0. Exit\n"))
    
    if char_input == 1:
        dec_to_bin()
    elif char_input == 2:
        bin_to_dec()
    elif char_input == 3:
        xor_cipher()
    elif char_input == 0:
        break
