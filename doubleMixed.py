# will choose
import math
import random

import Encoding


def main(source, randomness, maxKey, fromPaperEncoding, huffman, destination):  # maxKey > 3
    f = open(source, "r")  # edit path to file
    src = f.read()
    f.close()
    table1 = {}
    table2 = {}
    offs = [0, 0, 0, 0, 0]
    # randomness = True  # if True will choose a random table, instead of the maximal one
    # random.seed(10)
    lengths = {}
    # huffman = ["0000", "1", "01", "001", "0001"]
    bias = 0

    # will start at index start and finish and will step forward as long as the chars at these indices are identical
    def rollForward(start, finish):
        length = 0
        while True:
            if finish + length == len(src):  # if true it means the index is outside of the document
                return length
            # if length == 16:  # so that when we print the binary code the length int would be under 8 bit
            # return length
            if src[start + length] == src[finish + length]:  # check identical chars at these locations
                length = length + 1
            else:
                return length  # chars are dissimilar

    def updateTables(index, length):
        if len(src) - index <= maxKey:
            return
        for x in range(1, length):
            for keyLength in range(3, maxKey + 1):
                key = ""
                for counter in range(0, keyLength):
                    key += src[index - x + counter]
                table2.update({key: table1.get(key)})
                table1.update({key: index - x})

    # given a start index i will run backwards attempting to find the offset with the maximal length
    def find(index):  # current index we're at
        off1 = 0
        len1 = 0
        off2 = 0
        len2 = 0
        if len(src) - index > maxKey:  # not 1 last digits
            for x in range(maxKey, 2, -1):
                key = ""
                for counter in range(0, x):
                    key += src[index + counter]
                if table1.get(key) is not None:
                    len1 = rollForward(table1.get(key), index)
                    off1 = index - table1[key]
                    if off1 > 35137:
                        len1 = 0
                if table2.get(key) is not None:
                    len2 = rollForward(table2.get(key), index)
                    off2 = index - table2[key]
                    if off2 > 35137:
                        len2 = 0
                if len2 > len1:
                    len1 = len2
                    off1 = off2
                table2.update({key: table1.get(key)})
                table1.update({key: index})
                if len1 < 3:
                    len1 = 0
                if len1 > 0:
                    break
        return off1, len1

    if randomness:
        binary = open(destination + str(maxKey) + "BinRand.txt", "w")
        classic = open(destination + str(maxKey) + "ClaRand.txt", "w")
    else:
        binary = open(destination + str(maxKey) + "Bin.txt", "w")
        classic = open(destination + str(maxKey) + "Cla.txt", "w")

    index = 0
    while index < len(src)-1000:#len(src):
        findResult = find(index)
        if fromPaperEncoding:
            if randomness and random.random() > 0.5 and findResult[1] > 1:  # encoding call
                offs[Encoding.fromPaper(binary, [int(findResult[0] + bias), findResult[1] + 1], src[index], offs)] += 1
                Encoding.readable(classic, [int(findResult[0] + 8), findResult[1] + 1], src[index])
                bias = (bias * 2) % 16 + 1
            else:
                offs[Encoding.fromPaper(binary, findResult, src[index], offs)] += 1
                Encoding.readable(classic, findResult, src[index])
                bias = (bias * 2) % 16 + 0
        else:
            if randomness and random.random() > 0.5 and findResult[1] > 1:  # encoding call
                offs[Encoding.knownInAdvance(binary, [int(findResult[0] + bias), findResult[1] + 1], src[index],
                                             huffman)] += 1
                Encoding.readable(classic, [int(findResult[0] + bias), findResult[1] + 1], src[index])
                bias = (bias * 2) % 16 + 1
            else:
                offs[Encoding.knownInAdvance(binary, findResult, src[index], huffman)] += 1
                Encoding.readable(classic, findResult, src[index])
                bias = (bias * 2) % 16 + 0

        if findResult[1] > 0:
            index += findResult[1]
            updateTables(index, findResult[1])
            if lengths.get(findResult[1]) is None:
                lengths.update({findResult[1]: 1})
            else:
                tmp = lengths.get(findResult[1])
                lengths.update({findResult[1]: tmp + 1})
        else:
            index += 1
        print(index)

    classic.close()
    binary.close()
    #if randomness:
    #    lengthsFile = open(destination + str(maxKey) + "LensRand.txt", "w")
    #    offsFile = open(destination + str(maxKey) + "OffsRand.txt", "w")
    #else:
    #    lengthsFile = open(destination + str(maxKey) + "Lens.txt", "w")
    #    offsFile = open(destination + str(maxKey) + "Offs.txt", "w")
    #for x in sorted(lengths):
    #    lengthsFile.write(str(x) + "    " + str(lengths[x]) + "\n")
    #offsFile.write(offs.__str__())
    #offsFile.close()
    #lengthsFile.close()


# ###############################################################################################################################################################

def mainFlagged(source, randomness, maxKey, fromPaperEncoding, huffman, destination, flag):  # maxKey > 3
    f = open(source, "r")  # edit path to file
    src = f.read()
    f.close()
    table1 = {}
    table2 = {}
    offs = [0, 0, 0, 0, 0]
    # randomness = True  # if True will choose a random table, instead of the maximal one
    # random.seed(10)
    lengths = {}
    # huffman = ["0000", "1", "01", "001", "0001"]
    bias = 0

    # will start at index start and finish and will step forward as long as the chars at these indices are identical
    def rollForward(start, finish):
        length = 0
        while True:
            if finish + length == len(src):  # if true it means the index is outside of the document
                return length
            # if length == 16:  # so that when we print the binary code the length int would be under 8 bit
            # return length
            if src[start + length] == src[finish + length]:  # check identical chars at these locations
                length = length + 1
            else:
                return length  # chars are dissimilar

    def updateTables(index, length):
        if len(src) - index <= maxKey:
            return
        for x in range(1, length):
            for keyLength in range(3, maxKey + 1):
                key = ""
                for counter in range(0, keyLength):
                    key += src[index - x + counter]
                table2.update({key: table1.get(key)})
                table1.update({key: index - x})

    # given a start index i will run backwards attempting to find the offset with the maximal length
    def find(index):  # current index we're at
        off1 = 0
        len1 = 0
        off2 = 0
        len2 = 0
        if len(src) - index > maxKey:  # not 1 last digits
            for x in range(maxKey, 2, -1):
                key = ""
                for counter in range(0, x):
                    key += src[index + counter]
                if table1.get(key) is not None:
                    len1 = rollForward(table1.get(key), index)
                    off1 = index - table1[key]
                    if off1 > 35137:
                        len1 = 0
                if table2.get(key) is not None:
                    len2 = rollForward(table2.get(key), index)
                    off2 = index - table2[key]
                    if off2 > 35137:
                        len2 = 0
                if len2 > len1:
                    len1 = len2
                    off1 = off2
                table2.update({key: table1.get(key)})
                table1.update({key: index})
                if len1 < 3:
                    len1 = 0
                if len1 > 0:
                    break
        return off1, len1

    if randomness:
        binary = open(destination + str(maxKey) + "BinRand"+str(flag)+".txt", "w")
        classic = open(destination + str(maxKey) + "ClaRand"+str(flag)+".txt", "w")
    else:
        binary = open(destination + str(maxKey) + "Bin"+str(flag)+".txt", "w")
        classic = open(destination + str(maxKey) + "Cla"+str(flag)+".txt", "w")

    index = 0
    while index < len(src):
        findResult = find(index)
        if fromPaperEncoding:
            if findResult[1] > 1 and flag == 1:  # encoding call
                offs[Encoding.fromPaper(binary, [int(findResult[0] + bias), findResult[1] + 1], src[index], offs)] += 1
                Encoding.readable(classic, [int(findResult[0] + 8), findResult[1] + 1], src[index])
                bias = (bias * 2) % 16 + 1
                flag = -1
            elif findResult[1] > 1 and flag == 0:  # encoding call
                offs[Encoding.fromPaper(binary, [int(findResult[0]), findResult[1]], src[index],
                                        offs)] += 1
                Encoding.readable(classic, [int(findResult[0]), findResult[1]], src[index])
                bias = (bias * 2) % 16
                flag = -1
            elif randomness and random.random() > 0.5 and findResult[1] > 1 and flag == -1:  # encoding call
                offs[Encoding.fromPaper(binary, [int(findResult[0] + bias), findResult[1] + 1], src[index], offs)] += 1
                Encoding.readable(classic, [int(findResult[0] + 8), findResult[1] + 1], src[index])
                bias = (bias * 2) % 16 + 1
            else:
                offs[Encoding.fromPaper(binary, findResult, src[index], offs)] += 1
                Encoding.readable(classic, findResult, src[index])
                bias = (bias * 2) % 16 + 0
        else:
            if findResult[1] > 1 and flag == 1:  # encoding call
                offs[Encoding.knownInAdvance(binary, [int(findResult[0] + bias), findResult[1] + 1], src[index],
                                             huffman)] += 1
                Encoding.readable(classic, [int(findResult[0] + bias), findResult[1] + 1], src[index])
                bias = (bias * 2) % 16 + 1
                flag = -1
            elif findResult[1] > 1 and flag == 0:  # encoding call
                offs[Encoding.knownInAdvance(binary, [int(findResult[0] + bias), findResult[1]], src[index],
                                             huffman)] += 1
                Encoding.readable(classic, [int(findResult[0] + bias), findResult[1] + 1], src[index])
                bias = (bias * 2) % 16
                flag = -1
            elif randomness and random.random() > 0.5 and findResult[1] > 1 and flag == -1:  # encoding call
                offs[Encoding.knownInAdvance(binary, [int(findResult[0] + bias), findResult[1] + 1], src[index],
                                             huffman)] += 1
                bias = (bias * 2) % 16 + 1
                flag = -1
            else:
                offs[Encoding.knownInAdvance(binary, findResult, src[index], huffman)] += 1
                Encoding.readable(classic, findResult, src[index])
                bias = (bias * 2) % 16 + 0

        if findResult[1] > 0:
            index += findResult[1]
            updateTables(index, findResult[1])
            if lengths.get(findResult[1]) is None:
                lengths.update({findResult[1]: 1})
            else:
                tmp = lengths.get(findResult[1])
                lengths.update({findResult[1]: tmp + 1})
        else:
            index += 1
        print(index)

    classic.close()
    binary.close()
    #if randomness:
    #    lengthsFile = open(destination + str(maxKey) + "LensRand.txt", "w")
    #    offsFile = open(destination + str(maxKey) + "OffsRand.txt", "w")
    #else:
    #    lengthsFile = open(destination + str(maxKey) + "Lens.txt", "w")
    #    offsFile = open(destination + str(maxKey) + "Offs.txt", "w")
    #for x in sorted(lengths):
    #    lengthsFile.write(str(x) + "    " + str(lengths[x]) + "\n")
    #offsFile.write(offs.__str__())
    #offsFile.close()
    #lengthsFile.close()
