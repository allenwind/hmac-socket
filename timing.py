def compare_digest(text1, text2):
    if len(text1) != len(text2):
        return False
    r = 0
    for x, y in zip(text1, text2):
        r |= ord(x) ^ ord(y)
    return r == 0

def basic_compare(text1, text2):
    if len(text1) != len(text2):
        return False

    for s1, s2 in zip(text1, text2):
        if s1 != s2:
            return False
    return True
