import datetime


def years(age, name, copy):
    today = datetime.date.today()
    time = 100 - age
    print(
        (name + ", you will reach 100 at " +
         str(today.year + time) + ".\n") * copy)
    return


def main():
    name = input("Type your name!")
    age = int(input("How old are you?"))
    copy = int(input("How many copies do you want?"))
    years(age, name, copy)
    return


if __name__ == '__main__':
    main()
