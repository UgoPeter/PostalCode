from PostalCodeGenerator import generator

if __name__ == '__main__':
    postalCodeStart = input("Please enter the beginning of your list of postal codes: ")
    postalCodeEnd = input("Please enter the end of a list of postal codes: ")
    a = generator(postalCodeStart, postalCodeEnd)
    print(*generator(postalCodeStart, postalCodeEnd), sep=", ")
