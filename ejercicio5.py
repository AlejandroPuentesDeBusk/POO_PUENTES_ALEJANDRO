def main():

    while True:
        try:
            age = int(input("What's your age?"))

            if age >= 18:
                print("Get in")
            else:
                print("You shouldn't be here")
                
            break
                
        except ValueError:
            print("Incorrect data type")

main()
