def decode(source, destination, huffs):
    offs = [0, 6, 8, 11, 15]
    offAdded = [0, 1, 65, 321, 2369]

    def getChar(text, textIndex):
        bob = 0
        for x in range(0, 8):
            bob *= 2
            bob += int(text[textIndex + x])
            textIndex + 1
        return chr(bob)

    def getOff(text, textIndex, huff):
        # print(text[textIndex: textIndex + 20])
        bob = 0
        for x in range(0, offs[huff]):
            # print(text[textIndex])
            bob *= 2
            bob += int(text[textIndex])
            textIndex += 1
        # print(bob + offAdded[huff])
        return bob + offAdded[huff], textIndex

    def getLen(text, textIndex, out, index, off):
        # print(text[textIndex: textIndex + 20])
        x = 0
        while text[textIndex] != "0":  # finding j+1 = x, i.e. amount of preceding 1's
            # print(text[textIndex: textIndex + 20])
            x += 1
            textIndex += 1
        textIndex += 1  # skipping over 0
        # print(text[textIndex: textIndex + 20])
        j = x - 1
        if j < 0:
            j = 0
        bob = 0
        # print(text[textIndex: textIndex + 20])
        for y in range(0, j):  # figuring out the binary of length j
            bob *= 2
            # bob += int(text[textIndex + x])
            bob += int(text[textIndex])
            textIndex += 1
        # print(j)
        # print(textIndex)
        # print(text[textIndex: textIndex + 20])
        for z in range(0, bob + 2 + (2 ** j)):  # copying the actual number of chars needed
            #if out[index - off] == '\x80':
            #    print(out[index - off-5:index - off+5])
            #    print(index-off)
            #    print(out[index - off])
            #    print(ord(out[index - off]))
            #    print("YOYOYOYOYOOYYOOYYOOYOYOY")
            out += out[index - off]
            index += 1
        # print(textIndex)
        return (bob + 2 + (2 ** j)), textIndex, index, out,

    ############################ main ########################
    f = open(source, "r")
    count = 0
    text = f.read()
    f.close()
    out = ""
    index = 0
    textIndex = 0
    outLen = 0
    huffInterpreter = ""
    huff = -1
    textLen = len(text)
    while textIndex < 1000000:
    #while textIndex < 1000:
        #print(text[textIndex:textIndex+30])
        print(textIndex)
        #print(textLen)
        # if outLen >= 20:
        #     print("")
        # for z in range(40):
        #if index > 2780:
        #    print(text[textIndex:textIndex + 60])
        while huff == -1:
            huffInterpreter += text[textIndex]
            textIndex += 1
            if huffInterpreter == huffs[0]:
                huff = 0
            if huffInterpreter == huffs[1]:
                huff = 1
            if huffInterpreter == huffs[2]:
                huff = 2
            if huffInterpreter == huffs[3]:
                huff = 3
            if huffInterpreter == huffs[4]:
                huff = 4
        if huff == 0:
            out += getChar(text, textIndex)
            outLen += 1
            textIndex += 8
            index += 1
        else:
            getOffRes = getOff(text, textIndex, huff)
            off = getOffRes[0]
            textIndex = getOffRes[1]
            if off >index:
                off = 10
            getLenRes = getLen(text, textIndex, out, index, off)
            outLen += getLenRes[0]
            textIndex = getLenRes[1]
            index += getLenRes[0]
            out = getLenRes[3]
            # out += out[index - off: index - off + length]
        huff = -1
        huffInterpreter = ""
        #print(index)
    print(out)
    f = open(destination, "w")
    f.write(out)
    f.close()
