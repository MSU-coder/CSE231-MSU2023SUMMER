
if __name__ == '__main__':
    quarters = 10
    dimes = 10
    nickels = 10
    pennies = 10

    print("Welcome to change-making program.")
    print("Stock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
        quarters, dimes, nickels, pennies))

    while True:
        in_str = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")

        if in_str == 'q':
            break

        elif float(in_str) < 0:
            print("Error: purchase price must be non-negative.")
            continue

        else:
            price = int(float(in_str) * 100)  # Convert to cents
            paid = int(input("Input dollars paid (int): ")) * 100  # Convert to cents

            while paid < price:
                print("Error: insufficient payment.")
                paid = int(input("Input dollars paid (int): ")) * 100  # Convert to cents

            change = paid - price
            if change == 0:
                print("No change.")
            else:
                q, change = divmod(change, 25)
                if q > quarters:
                    q, change = quarters, change + (q-quarters)*25
                quarters -= q

                d, change = divmod(change, 10)
                if d > dimes:
                    d, change = dimes, change + (d-dimes)*10
                dimes -= d

                n, change = divmod(change, 5)
                if n > nickels:
                    n, change = nickels, change + (n-nickels)*5
                nickels -= n

                p = change
                if p > pennies:
                    print("Error: ran out of coins.")
                    break
                pennies -= p

                print("Collect change below:")
                if q > 0:
                    print("Quarters:", q)
                if d > 0:
                    print("Dimes:", d)
                if n > 0:
                    print("Nickels:", n)
                if p > 0:
                    print("Pennies:", p)

        print("Stock: {} quarters, {} dimes, {} nickels, and {} pennies".format(
            quarters, dimes, nickels, pennies))

    print("Goodbye.")
