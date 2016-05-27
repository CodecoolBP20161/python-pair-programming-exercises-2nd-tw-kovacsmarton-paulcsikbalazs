def palindrome(string):
    fine_word = string.replace(" ", "")
    lower = fine_word.lower()
    if lower == lower[::-1]:
        print("This is a 'palindrome'!")
        return True
    else:
        print("This is not a 'palindrome'!")
        return False


def main():
    word = input("Please type your 'palindrome!'")
    palindrome(word)


if __name__ == '__main__':
    main()
