import datetime


def years(age):
    today = datetime.date.today()
    return 100 - age + today.year


def main():
    name = input("Type your name! ")
    age = int(input("How old are you? "))
    copy = int(input("How many copies do you want? "))
    print((name + ", you will reach 100 at " + str(years(age)) + ".\n") * copy)
    years(age)


if __name__ == '__main__':
    main()
