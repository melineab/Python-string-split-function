def split(txt: str, sep: str) -> list:
    res = []
    if len(sep) <= 0:
        raise ValueError(' The separator must contain '
                         'at least one character.')
    start = 0
    while True:
        idx = txt.find(sep, start, len(txt))
        if idx != -1:
            res.append(txt[start:idx])
            start = idx + len(sep)
        else:
            res.append(txt[start:len(txt)])
            break
    return res


if __name__ == "__main__":
    print(split(' hello there  my dear friends !!!', '  '))
    print(' hello there  my dear friends !!!'.split('  '))
