# simple calculator

print("a = Add | s = subtract | d = Divide | m = multiply")
opCode = input("Select a function: ")

if (opCode == "a" or "b" or "d" or "m"):
    x1 = float(input("Select a number: "))
    x2 = float(input("select another number: "))

    if (opCode == "a"):
        ans = (x1 + x2)
    elif (opCode == "s"):
        ans = (x1 - x2)
    elif (opCode == "d"):
        ans = (x1/x2)
    elif (opCode == "m"):
        ans = (x1 * x2)
    else:
        print("Unknown command error")

    print(ans)
