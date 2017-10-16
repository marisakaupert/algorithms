def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Add the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))

print(int_to_string(-314))


def string_to_int(s):
    pass


