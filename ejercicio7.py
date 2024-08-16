def main():

    while True:
        try:
            w = float(input("Package weight: "))
            
            if w < 1:
                print("delivery cost = $50")
            elif w >= 1 and w < 5:
                print("delivery cosst = $100")
            elif w >= 5 and w <10:
                print("delivery cosst = $200")
            else:
                print("delivery cosst = $500")

            break

        except ValueError:
            print("Incorrect data type")
main()