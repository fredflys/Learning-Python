def chinese(str):
    count = 0
    for char in str:
        if ord(char) > 127:
            count += 1
    return count


def format_str(str, length):
    count = chinese(str)
    # fillin_spaces = (length - count * 2) * ' '
    # return str + fillin_spaces
    fmtted_str = '{0:{remain}}'.format(str, remain=length-count)
    return fmtted_str