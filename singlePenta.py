import random

import Encoding


def main(source, randomness):
    f = open(source, "r")  # edit path to file
    src = f.read()
    f.close()
    table = {}
    # randomness = False  # change to true to allow random choice of table at each
    # random.seed(10)
    lengths = {}
    offs = [0, 0, 0, 0, 0]

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
        if len(src) - index <= 5:
            return
        for x in range(1, length):
            key = src[index - x] + src[index - x + 1] + src[index - x + 2] + src[index - x + 3] + src[index - x + 4]
            table.update({key: index - x})

    # given a start index i will run backwards attempting to find the offset with the maximal length
    def find(index):  # current index we're at
        finalOff = 0
        finalLength = 0
        if len(src) - index > 5:  # not 2 last digits
            key = src[index] + src[index + 1] + src[index + 2] + src[index + 3] + src[index + 4]
            if table.__contains__(key):
                finalLength = rollForward(table[key], index)
                finalOff = index - table[key]
                if finalOff > 35137:
                    finalLength = 0
            table.update({key: index})
            if finalLength > 4 and randomness:
                if random.random() > 0.5:
                    finalLength -= 1
        return finalOff, finalLength

    if randomness:
        binary = open("files/out/singlePenta/outBinRand.txt", "w")
        classic = open("files/out/singlePenta/outClaRand.txt", "w")
    else:
        binary = open("files/out/singlePenta/outBin.txt", "w")
        classic = open("files/out/singlePenta/outCla.txt", "w")
    # of off|len
    index = 0
    while index < len(src):
        findResult = find(index)
        offs[Encoding.fromPaperBin(binary, findResult, src[index])] += 1
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
        lengthsFile = open("files/out/singlePenta/lengthsRand.txt", "w")
        offsFile = open("files/out/singlePenta/offsRand.txt", "w")
    else:
        lengthsFile = open("files/out/singlePenta/lengths.txt", "w")
        offsFile = open("files/out/singlePenta/offs.txt", "w")

    for x in sorted(lengths):
        lengthsFile.write(str(x) + "    " + str(lengths[x]) + "\n")
    offsFile.write(offs.__str__())
    offsFile.close()
    lengthsFile.close()

# print(table)
