# pip install pycodestyle

import sys 
print(sys.argv)

if len(sys.argv) > 1:
    str = sys.argv[1]
    i = 2
    while i < len(sys.argv):
        str = str + " " + sys.argv[i]
        i += 1
    str_rev = str[::-1]
    print(str_rev.swapcase())