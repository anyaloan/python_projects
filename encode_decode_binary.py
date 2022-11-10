##################Decodefunction###################

def decode_string(mstr: str) -> str:
    binary_list = []
    nstr = ""
    my_ind = 0
    for el in mstr:
        nstr = f'{nstr}{el}'
        my_ind += 1
        if my_ind % 8 == 0:
            binary_list.append(nstr)
            nstr = ''
    decimal_list = [int(el, 2) for el in binary_list]
    nl = [chr(el) for el in decimal_list]
    return "".join(nl)


print(decode_string("0100100001100101011011000110110001101111"))


#######Encodefunction####################


def encode_string(mstr: str) -> str:
    ml = [ord(el) for el in mstr]
    encoded_list = []
    for el in ml:
        el = bin(el)
        if len(str(el)) == 9:
            el = f"0{el[2:]}"
        elif len(str(el)) == 8:
            el = f"00{el[2:]}"
        encoded_list.append(el)
    return "".join(encoded_list)


print(encode_string("Hello"))
