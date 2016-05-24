a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def list_overlap(list1, list2):
    seta = set(list1)
    setb = set(list2)
    set_full = seta & setb
    mylist = list(set_full)
    print(mylist)
    return mylist



def main():
    list_overlap(a, b)
    return


if __name__ == '__main__':
    main()
