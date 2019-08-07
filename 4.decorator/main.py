def file_write(filename):
    def outer(func):
        def wrapper(res):
            f = open(filename, 'a')
            f.write(str(func(res)) + '\n')
            return func(res)

        return wrapper

    return outer


@file_write('example.txt')
def get_easy_unique(rand_list):
    unique = list(set(rand_list))
    return unique


def main():
    num_list = [1, 1, 2, 3, 5, 4, 5, 5, 6]
    unique = get_easy_unique(num_list)
    print(unique)


if __name__ == '__main__':
    main()
