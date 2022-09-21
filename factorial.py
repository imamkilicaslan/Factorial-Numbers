while True:
    number = int(input("input a number \n"))

    result = 1

    if number >= 0:
        for i in range(0, number):
            result *= number
            number -= 1

        print(result)
    else:
        print("cannot be a negative factorial")
