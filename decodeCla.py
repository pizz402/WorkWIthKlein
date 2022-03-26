def decode(source, destination):
    f = open(source, "r")
    count =0
    text = f.read()
    f.close()
    out = ""
    index = 0
    textIndex = 0
    outLen = 0
    textLen = len(text)
    while textIndex <= textLen:
    #for z in range(40):
        if textIndex < textLen - 10000000 and text[textIndex] == " " and text[textIndex+1] == "(":
            if text[textIndex + 2] == "o" and text[textIndex + 3] == "f" and text[textIndex + 4] == "f" and text[
                textIndex + 5] == ":" and text[textIndex + 6] == " ":
                print(textIndex)
                #print("0 - " + str(textIndex) + text[textIndex])
                #print("1 - " + str(textIndex) + text[textIndex +1])
                #print("2 - " + str(textIndex) + text[textIndex +2])
                #print("3 - " + str(textIndex) + text[textIndex +3])
                #print("4 - " + str(textIndex) + text[textIndex +4])
                #print("5 - " + str(textIndex) + text[textIndex +5])
                #print("6 - " + str(textIndex) + text[textIndex +6])
                off = 0
                x = 0
                while 48 <= ord(text[textIndex + 7 + x]) <= 57:
                    off *= 10
                    off += ord(text[textIndex + + 7 + x]) - 48
                    x += 1
                if text[textIndex + 7 + x] != ",":
                    out += text[textIndex]
                    textIndex += 1
                    break
                if text[textIndex + 8 + x] != " ":
                    out += text[textIndex]
                    textIndex += 1
                    break
                if text[textIndex + 9 + x] != "l":
                    out += text[textIndex]
                    textIndex += 1
                    break
                if text[textIndex + 10 + x] != "e":
                    out += text[textIndex]
                    textIndex += 1
                    break
                if text[textIndex + 11 + x] != "n":
                     out += text[textIndex]
                     textIndex += 1
                     break
                if text[textIndex + 12 + x] != ":":
                    out += text[textIndex]
                    textIndex += 1
                    break
                if text[textIndex + 13 + x] != " ":
                    out += text[textIndex]
                    textIndex += 1
                    break
                length = 0
                while 48 <= ord(text[textIndex + 14 + x]) <= 57:
                    length *= 10
                    length += ord(text[textIndex + 14 + x]) - 48
                    x += 1
                if text[textIndex + 14 + x] != ")":
                    out += text[textIndex]
                    index += 1
                    break
                if text[textIndex + 15 + x] != " ":
                    out += text[textIndex]
                    index += 1
                    break
                for y in range(0,length):
                    out += text[textIndex-off+y]
                outLen += length
                #index += x + 15
                textIndex += x + 15
                count += 1
            else:
                out += text[textIndex]
                index += 1
                textIndex += 1
                break
        else:
            print(textIndex)
            out += text[textIndex]
            index += 1
            textIndex += 1
            if textIndex > textLen - 10000000:
                break
    f = open(destination, "w")
    f.write(out)
    f.close()
    print(count)
