#Decoding lab

#Menu function
def Menu():
    print(f"Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n")
    Selection=int(input("Please enter an option: "))
    if Selection==1:
        HexCode=str(input("Please enter the numeric string to convert: "))
        print(f"Result: {hex_string_decode(HexCode)}\n")
        Menu()
    elif Selection==2:
        BinCode=str(input("Please enter the numeric string to convert: "))
        print(f"Result: {binary_string_decode(BinCode)}\n")
        Menu()
    elif Selection==3:
        BinCode=str(input("Please enter the numeric string to convert: "))
        print(f"Result: {binary_to_hex(BinCode)}\n")
        Menu()
    elif Selection==4:
        print("Goodbye!")
    else:
        print("Invalid selection\n")
        Menu()

#Hex string decoder function
def hex_string_decode(hex):
    NewHex = ""
    Decimal = 0
    i = 0
    if "0x" in hex:
        NewHex+=hex[2:]
    else:
        NewHex+=hex[:]
    for digit in NewHex[::-1]:
        Decimal+=(hex_char_decode(digit) * 16**i)
        i+=1
    return Decimal

#Hex digit decoder function
def hex_char_decode(digit):
    #If the digit is not a number, just set it out of range for the first condition
    try:
        Num=int(digit)
    except:
        Num=10
    if 0<=Num<=9:
        return Num
    elif digit.lower()=="a":
        return 10
    elif digit.lower() == "b":
        return 11
    elif digit.lower() == "c":
        return 12
    elif digit.lower() == "d":
        return 13
    elif digit.lower() == "e":
        return 14
    elif digit.lower() == "f":
        return 15

#Binary decoder function
def binary_string_decode(binary):
    NewBin=""
    Decimal=0
    i = 0
    if "0b" in binary:
        NewBin+=binary[2:]
    else:
        NewBin+=binary[:]
    for digit in NewBin[::-1]:
        Decimal+=(int(digit)*2**i)
        i+=1
    return Decimal

#Binary to hex function
def binary_to_hex(binary):
    NewBin=""
    Quadple, i = 0, -1
    Hex=""
    if "0b" in binary:
        NewBin+=binary[2:]
    else:
        NewBin+=binary[:]
    for digit in NewBin[::-1]:
        if i > 2:
            Hex+=DecToHex(Quadple)
            Quadple, i = 0, -1
        i+=1
        Quadple+=(int(digit)*2**i)
    Hex+=DecToHex(Quadple)
    return Hex[::-1]

#Decimal values to hex
def DecToHex(dec):
    if 0<=dec<=9:
        return str(dec)
    elif dec==10:
        return "A"
    elif dec==11:
        return "B"
    elif dec==12:
        return "C"
    elif dec==13:
        return "D"
    elif dec==14:
        return "E"
    elif dec==15:
        return "F"

Menu()