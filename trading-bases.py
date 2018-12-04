#! /usr/bin/env python3
# changing bases for IP address management 

from sys import argv

class SubnetConversion():
    def main(self):

        global theNum
        mode = argv[1]
    
        theNum = input("Enter address to to convert to {}: ".format(mode))
        if mode.lower() == "db":
            SubnetConversion.dec_to_bin(self, theNum)
        elif mode.lower() == "bd":
            SubnetConversion.bin_to_dec(self, theNum)
        elif mode.lower() == "dh":
            SubnetConversion.dec_to_hex(self, theNum)
        elif mode.lower() == "hd":
            SubnetConversion.hex_to_dec(self, theNum)
        elif mode.lower() == "hb":
            SubnetConversion.hex_to_bin(self, theNum)
        elif mode.lower() == "bh":
            SubnetConversion.bin_to_hex(self, theNum)

        
    def dec_to_bin(self, number):
        binum = bin(int(number))
        print(str(binum)[2:])

    def bin_to_dec(self, number):
        bdnum = int((number), 2)
        print(bdnum)

    def dec_to_hex(self, number):
        dhnum = hex(int(number))
        print(str(dhnum)[2:])
    
    def hex_to_dec(self, number):
        hdnum = int(number, 16)
        print(hdnum)

    def hex_to_bin(self, number):
        print(bin(int(number,16)))

    def bin_to_hex(self, number):
        bhnum = hex(int(number,2))
        print(bhnum)
    

SubnetInst = SubnetConversion()

if __name__ == '__main__':
    SubnetInst.main()
