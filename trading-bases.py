#! /usr/bin/env python3
# changing bases for IP address management 

from sys import argv

def main():
    global theNum
    global mode

    mode = argv[1]
    theNum = input("Enter address to to convert to {}: ".format(mode))

    if "." in theNum:
        concat = ""
        theNum = theNum.split(".")
        #print("theNum list is :", theNum)

        for i in theNum:
            #print("Value for this loop:", i)
            #print("concat: ", concat)
            #print("value from converstion:", conversion(i))
            concat = concat + str(conversion(i)) + "."
        concat = concat[:-1]
        return concat

    elif ":" in theNum:
        concat = ""
        theNum = theNum.split(":")

        for i in theNum:
            concat = concat + str(conversion(i)) + ":"
            concat = concat[:-1]
        return concat

    else:
        return conversion(theNum)


def conversion(number):
    if mode.lower() == "db":
        #print("number passed to conversion", number)
        return(dec_to_bin(number))
    elif mode.lower() == "bd":
        return bin_to_dec(number)
    elif mode.lower() == "dh":
        return dec_to_hex(number)
    elif mode.lower() == "hd":
        return hex_to_dec(number)
    elif mode.lower() == "hb":
        return hex_to_bin(number)
    elif mode.lower() == "bh":
        return bin_to_hex(number)

        
def dec_to_bin(number):
    binum = bin(int(number))
    return str(binum)[2:]

def bin_to_dec(number):
    bdnum = int((number), 2)
    return bdnum

def dec_to_hex(number):
    dhnum = hex(int(number))
    return str(dhnum)[2:]
    
def hex_to_dec(number):
    hdnum = int(number, 16)
    return hdnum

def hex_to_bin(number):
    return bin(int(number,16))

def bin_to_hex(number):
    bhnum = hex(int(number,2))
    return bhnum
    

if __name__ == '__main__':
    print(main())
