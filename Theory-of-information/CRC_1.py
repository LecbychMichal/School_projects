def xor(a, b):
    result = []

    for i in range (1, len (b)):
        if a[i] == b[i]:
            result.append ('0')
        else:
            result.append ('1')

    return ''.join (result)

def crc(code, polynomial):

    g = len(polynomial)
    tmp = code[0:g]

    while g < len(code):

        if tmp[0] == "1":
            tmp = xor(polynomial, tmp) + code[g]
        else:
            tmp = xor("0"*g, tmp) + code[g]

        g += 1
    if tmp[0] == "1":
        tmp = xor(polynomial, tmp)
    else:
        tmp = xor("0"*g, tmp)

    remainder = tmp
    return remainder

def sender(information, polynomial):
    print("SENDER:")
    crc_check = "0" * (len (polynomial) - 1)
    code = information + crc_check
    remainder = crc(code, polynomial)
    coded_information = information + remainder

    print("Coded information:", coded_information)
    print ("Generating polynomial:", polynomial, "\n")
    reciever (coded_information, polynomial, crc_check)

def reciever(coded_information, polynomial, crc_check):
    print("RECIEVER:")
    # coded_information = "11010011101100101" # odkomentovat k nastavení chyby

    if crc(coded_information, polynomial) == crc_check:
        print("Transmission of code is ok")
    else:
        syndrome = crc(coded_information, polynomial)
        print ("Transmission of code", coded_information, "is wrong")
        print ("Code word syndrome:", syndrome)

        position = {"001" : 0,
                    "010" : 1,
                    "100" : 2,
                    "101" : 3,
                    "111" : 4,
                    "011" : 5,
                    "110" : 6}

        misstake = len(coded_information) - 1 - position[syndrome]
        if coded_information[misstake] == "0":
            coded_information = coded_information[:misstake ] + "1" + coded_information[misstake + 1:]
        else:
            coded_information = coded_information[:misstake] + "0" + coded_information[misstake + 1:]

        print("Misstake on position:", misstake)
        print("Correction:", coded_information)


information = "11010011101100"
polynomial = "1011"

sender(information, polynomial)