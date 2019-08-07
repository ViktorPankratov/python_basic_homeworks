def get_unique(rand_list):
    unique = []
    for elem in rand_list:
        if not unique.__contains__(elem):
            unique.append(elem)
    return unique


def get_easy_unique(rand_list):
    unique = list(set(rand_list))
    return unique


def main():
    num_list = [1, 1, 2, 3, 5, 4, 5, 5, 6]
    print(get_unique(num_list))
    print(get_easy_unique(num_list))


if __name__ == '__main__':
    main()
