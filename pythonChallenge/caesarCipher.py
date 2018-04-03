import string


def cipher(text):
    alphabet = string.ascii_lowercase
    result_string = ""
    for i, val in enumerate(text):
        if val in alphabet:
            if alphabet.index(val) == 24:
                result_index = 0
            elif alphabet.index(val) >= 25:
                result_index = 1
            else:
                result_index = alphabet.index(val) + 2
            result_string = result_string + alphabet[result_index]
        else:
            result_string = result_string + val

    print(result_string)


cipher("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
cipher("map")

# Next url:
# http://www.pythonchallenge.com/pc/def/ocr.html
