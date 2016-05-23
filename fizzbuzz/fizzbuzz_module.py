def fizzbuzz(number):
    if number % 15 == 0:
        number = 'FizzBuzz'
        print(number)
    elif number % 3 == 0:
        number = 'Fizz'
        print(number)
    elif number % 5 == 0:
        number = 'Buzz'
        print (number)
    else:
        print(number)
    return(number)


def main():
    for number in range(1, 101):
        fizzbuzz(number)

if __name__ == '__main__':
    main()
