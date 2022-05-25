def binary(deci):
    # deci = float(input("Enter num: "))
    rem = []
    while deci != 1:
        rem.append(int(deci%2))
        deci = int(deci/2)
    rem.append(int(deci%2))
    rem.reverse()
    bin = ""
    for i in range(0,len(rem)):
        bin = bin + str(rem[i])
    print("The binary code for entered number is",bin)