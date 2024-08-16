def main():

    while True:
        try:

            x = float(input("Type a number: "))
            y = float(input("Type another number: "))

            if x > y:
                print("X is grater than Y")

            elif y < x:
                print("Y is greater than X")

            else:
                print("X and Y are the same")

            break

        except ValueError:
            print("Provide a number")

main()