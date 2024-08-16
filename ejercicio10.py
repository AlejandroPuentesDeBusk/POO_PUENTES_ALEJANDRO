def main():

    while True:

        try:

            x = float(input("Type a number: "))

            y =float(input("Type a second number: "))

            print("Result = ", x+y)

            con= input(("Continue? y/n "))

            if con == "n":
                break
        

        except ValueError:

            print("Incorrect data type")

main()

         