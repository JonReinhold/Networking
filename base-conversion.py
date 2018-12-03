#! /usr/bin/env python3
# 

from sys import argv

class SubnetConversion():
    def main(self):
        global theNum
        mode = argv[1]

        theNum = int(input("Enter address to to convert to {}: ".format(mode)))
        if mode.lower() == "bin":
            SubnetConversion.dec_to_bin(self, theNum)
        elif mode.lower() == "dec":
            SubnetConversion.bin_to_dec(self, theNum)
        return ""
        
    def dec_to_bin(self, number):
        binum = bin(number)
        binum = (binum[2:])
        print(binum)
        return ""

    def bin_to_dec(self, number):
        decnum = int(str(number), 2)
        print(decnum)



SubnetInst = SubnetConversion()

if __name__ == '__main__':
    SubnetInst.main()
