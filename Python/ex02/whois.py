import sys

if len(sys.argv) != 3: # or isinstance(n, int)  or len(sys.argv) < 3
    print("Usage: python operations.py <number1> <number2> \n Example: \n python operations.py 10 3")
    exit(0)

try:
    int = int(sys.argv[1])
except ValueError:
    print("ERROR")
    exit(0)

if int < 0:
    print("ERROR")
    exit(0)

if int == 0:
    print("Je suis le zéro!")
    exit(0)
elif int % 2 == 0 :
    print("Je suis pair!")
    exit(0)
else: print("Je suis impair!")
exit(0)
