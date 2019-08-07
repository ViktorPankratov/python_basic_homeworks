def fizzbuzz(a, b, n):
    num_list = [x + 1 for x in range(n)]
    res = []
    for x in num_list:
        if not x % (a * b):
            x = 'fizzbuzz'
        elif not x % a:
            x = 'fizz'
        elif not x % b:
            x = 'buzz'
        res.append(x)

    return res


def main():
    print(fizzbuzz(3, 5, 100))


if __name__ == '__main__':
    main()
