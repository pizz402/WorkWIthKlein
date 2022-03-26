import random

import Encoding


def main(source, randomness, adaptive):
    f = open(source, "r")  # edit path to file
    src = f.read()
    f.close()
    table = {}
    # randomness = False  # change to true to allow random choice of table at each
    # random.seed(10)
    lengths = {}
    offs = [0, 0, 0, 0, 0]
    huffman = ["1000", "11", "0", "101", "1001"]

    # random.seed(10)

    # will start at index start and finish and will step forward as long as the chars at these indices are identical
    def rollForward(start, finish):
        length = 0
        while True:
            if finish + length == len(src):  # if true it means the index is outside of the document
                return length
            # if length == 16:  # so that when we print the binary code the length int would be under 8 bit
            #	return length
            if src[start + length] == src[finish + length]:  # check identical chars at these locations
                length = length + 1
            else:
                return length  # chars are dissimilar

    def updateTable(index, length):
        if len(src) - index <= 4:
            return
        for x in range(1, length):
            key = src[index - x] + src[index - x + 1] + src[index - x + 2] + src[index - x + 3]
            table.update({key: index - x})

    # given a start index i will run backwards attempting to find the offset with the maximal length
    def find(index):  # current index we're at
        finalOff = 0
        finalLength = 0
        if len(src) - index > 4:  # not 2 last digits
            key = src[index] + src[index + 1] + src[index + 2] + src[index + 3]
            if table.__contains__(key):
                finalLength = rollForward(table[key], index)
                finalOff = index - table[key]
                if finalOff > 35137:
                    finalLength = 0
            table.update({key: index})
            # if finalLength > 4 and randomness:
            #    if random.random() > 0.5:
            #        finalLength -= 1
        return finalOff, finalLength

    if randomness:
        binary = open("files/out/singleQuad/outBinRand.txt", "w")
        classic = open("files/out/singleQuad/outClaRand.txt", "w")
    else:
        binary = open("files/out/singleQuad/outBin.txt", "w")
        classic = open("files/out/singleQuad/outCla.txt", "w")
    # of off|len
    index = 0
    while index < len(src):
        findResult = find(index)
        if adaptive:
            if randomness and random.random() > 0.5 and findResult[1] > 0:  # encoding call
                offs[Encoding.adaptive(binary, [int(findResult[0] + 8), findResult[1] + 1], src[index], offs)] += 1
                Encoding.readable(classic, [int(findResult[0] + 8), findResult[1] + 1], src[index])
            else:
                offs[Encoding.adaptive(binary, findResult, src[index], offs)] += 1
                Encoding.readable(classic, findResult, src[index])
        else:
            if randomness and random.random() > 0.5 and findResult[1] > 0:  # encoding call
                offs[Encoding.knownInAdvance(binary, [int(findResult[0] + 8), findResult[1] + 1], src[index], huffman)] += 1
                Encoding.readable(classic, [int(findResult[0] + 8), findResult[1] + 1], src[index])
            else:
                offs[Encoding.knownInAdvance(binary, findResult, src[index], huffman)] += 1
                Encoding.readable(classic, findResult, src[index])

        if findResult[1] > 0:
            index += findResult[1]
            updateTable(index, findResult[1])
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
    if randomness:
        lengthsFile = open("files/out/singleQuad/lengthsRand.txt", "w")
        offsFile = open("files/out/singleQuad/offsRand.txt", "w")
    else:
        lengthsFile = open("files/out/singleQuad/lengths.txt", "w")
        offsFile = open("files/out/singleQuad/offs.txt", "w")

    for x in sorted(lengths):
        lengthsFile.write(str(x) + "    " + str(lengths[x]) + "\n")
    offsFile.write(offs.__str__())
    offsFile.close()
    lengthsFile.close()

# print(table)
