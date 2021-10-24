import math


def dec_to_bin(dec):
    string = ''
    while dec >= 1:
        bin_ = math.floor(dec % 2)
        string += str(bin_)
        dec = dec / 2
    print(string[::-1])


def bin_to_dec():
    dec = 0
    while True:
        try:
            bin_int = int(input("Введите двоичное число: "))
            bit_list = list(str(bin_int))

            for i in list(str(bin_int)):
                if i != '1' and i != '0':
                    raise ValueError
        except ValueError:
            print("Введите двоичное число ")
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
    message = list(str(input("Введите сообщение: ")))
    key = list(str(input("Введите ключ: ")))

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
    print("Закодированное сообщение: ", encode_result)    # I have to print a list of numbers, not an array of numbers

    # decode result
    for i in range(len(encode_result)):
        decode_result.append(chr(encode_result[i] ^ key_list[i]))
    print("Раскодированное сообщение: ", ''.join(decode_result))


xor_cipher()
