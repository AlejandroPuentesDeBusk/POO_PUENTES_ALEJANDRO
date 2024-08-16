def main():

    while True:
        try:
            psw = str(input("Password: "))

            if psw == "POO123":
                print("Logged in")
                break


        except ValueError:
            print("Incorrect password")
main()