def invert_dict_iter(d):
    try:
        y = {}
        for x in d:
            x, y[x] = d[x], x
    except TypeError as err:
        print('Impossible to invert: {}'.format(err))
        return
    return y


def invert_dict_gen(d):
    try:
        y = {d[x]: x for x in d}
    except TypeError as err:
        print('Impossible to invert: {}'.format(err))
        return
    return y


def main():
    d = {'key1': 'value1', 'key2': 'value2'}
    d_err = {'key1': 'value1', 'key2': {'key3': 'value3'}}
    print(invert_dict_iter(d_err))
    print(invert_dict_gen(d_err))
    print(invert_dict_gen(d))


if __name__ == '__main__':
    main()
