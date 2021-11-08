import sys

def usage(): print("Usage: python operations.py <number1> <number2> \n Example: \n python operations.py 10 3")

if len(sys.argv) != 3: # or isinstance(n, int)  or len(sys.argv) < 3
    if len(sys.argv) < 3:
        usage()
        exit(0)
    else: print("Too many arguments \n Usage: python operations.py <number1> <number2> \n Example: \n python operations.py 10 3")

try:
    int1 = int(sys.argv[1])
    int2 = int(sys.argv[2])
except ValueError:
    print("InputError: only numbers")
    usage()
    exit(0)

if int1 < 0 or int2 < 0:
    print("only positive numbers")
    usage()
    exit(0)

print("Sum:        ", int1 + int2)
print("Difference: ", int1 - int2)
print("Product:    ", int1 * int2)
if int2 == 0:
    print("Quotient:   ERROR (div by zero)")
    print("Reminder:   ERROR (modulo by zero)")
else: print("Quotient:   ", int1 / int2); print("Reminder:   ", int1 % int2)