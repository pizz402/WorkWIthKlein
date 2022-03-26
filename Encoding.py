from math import log2
import numpy as numpy
import copy

#def getIndexOfSmallestElement(offs, last):  # last =0 for smallest | last =1 for 2nd smallest :
#    count = 0
#    for off in offs:
#        if offs[index] > off:
#            count += 1
#    return count


def findMinIndex(offs):
    tmp = offs[0]
    index = 0
    for x in range(0, len(offs)):
        if offs[x] < tmp:
            tmp = offs[x]
            index = x
    return index

def getLengthOfHuffEncoding(offs, index):
    offsLocal = copy.copy(offs)
    count =0
    for x in range (0,4):
        #s1 = offsLocal.index(findMinIndex(offsLocal))
        s1 = findMinIndex(offsLocal)
        tmp = copy.copy(offsLocal)
        tmp.remove(offsLocal[s1])
        #print(tmp)
        #s2 = offsLocal.index(findMinIndex(tmp))
        s2 = findMinIndex(tmp)
        if s2 >= s1:
            s2 +=1
        if index == s1 or index == s2:
            count +=1
            tmp = offsLocal[s1] + offsLocal[s2]
            offsLocal[s1]= 99999999999
            offsLocal[s2] = offsLocal[s1]
            offsLocal[index] = tmp
        else:
            offsLocal[s1] = offsLocal[s1] + offsLocal[s2]
            offsLocal[s2] =99999999999
    return count

def findI(offs, index):
    count = 0
    for off in offs:
        if offs[index] > off:
            count += 1
    return count


def adaptive(destination, offLen, char, offs):  # offLen is (off, len)
    ret = None
    if offLen[1] > 0:
        str1 = ""
        if 1 <= offLen[0] <= 64:  # offs
            str1 = (getLengthOfHuffEncoding(offs, 1) * "0") + "{0:06b}".format(offLen[0])  # 1B_6(d-1)
            ret = 1
        elif 64 < offLen[0] <= 320:
            str1 = (getLengthOfHuffEncoding(offs, 2) * "0") + "{0:08b}".format(offLen[0] - 65)  # 01B_8(d-65)
            ret = 2
        elif 320 < offLen[0] <= 2368:
            str1 = (getLengthOfHuffEncoding(offs, 3) * "0") + "{0:011b}".format(offLen[0] - 321)  # 001B_11(d-321)
            ret = 3
        else:
            str1 = (getLengthOfHuffEncoding(offs, 4) * "0") + "{0:015b}".format(
                offLen[0] - 2369)  # 000B_15(d-2369) max off is 35,137
            ret = 4
        str2 = ""
        if offLen[1] == 2:  # length
            str2 = "0"
        else:
            j = int(log2(offLen[1] - 2))
            formatInfo = "{0:0" + str(j) + "b}"
            str2 = "1" * (j + 1) + "0" + formatInfo.format(offLen[1] - 2 - 2 ** j)
        destination.write(str1)
        destination.write(str2)
    else:
        destination.write((getLengthOfHuffEncoding(offs, 0) * "0") + "{0:08b}".format(ord(char)))
        ret = 0
    return ret


def knownInAdvance(destination, offLen, char, huffman):    #remove # from this
    ret = None
    if offLen[1] > 0:
        str1 = ""
        if 1 <= offLen[0] <= 64:  # offs
            str1 = huffman[1] + "{0:06b}".format(offLen[0]-1)  # 1B_6(d-1)
            ret = 1
        elif 64 < offLen[0] <= 320:
            str1 = huffman[2] + "{0:08b}".format(offLen[0] - 65)  # 01B_8(d-65)
            ret = 2
        elif 320 < offLen[0] <= 2368:
            str1 = huffman[3] + "{0:011b}".format(offLen[0] - 321)  # 001B_11(d-321)
            ret = 3
        else:
            str1 = huffman[4] + "{0:015b}".format(offLen[0] - 2369)  # 000B_15(d-2369) max off is 35,137
            ret = 4
        str2 = ""
        if offLen[1] == 2:  # length
            str2 = "0"
        else:
            j = int(log2(offLen[1] - 2))
            if j == 0:
                str2 = "1" * (j + 1) + "0"
            else:
                formatInfo = "{0:0" + str(j) + "b}"
                str2 = "1" * (j + 1) + "0" + formatInfo.format(offLen[1] - 2 - (2 ** j))
        destination.write(str1)
        destination.write(str2)
    else:
        destination.write(huffman[0] + "{0:08b}".format(ord(char)))
        ret = 0
    return ret

def fromPaper(destination, offLen, char, huffman):
    ret = None
    if offLen[1] > 0:
        str1 = ""
        if 1 <= offLen[0] <= 64:  # offs
            str1 = "10" + "{0:06b}".format(offLen[0]-1)  # 1B_6(d-1)
            ret = 1
        elif 64 < offLen[0] <= 320:
            str1 = "110" + "{0:08b}".format(offLen[0] - 65)  # 01B_8(d-65)
            ret = 2
        elif 320 < offLen[0] <= 2368:
            str1 = "1110" + "{0:011b}".format(offLen[0] - 321)  # 001B_11(d-321)
            ret = 3
        else:
            str1 = "1111" + "{0:015b}".format(offLen[0] - 2369)  # 000B_15(d-2369) max off is 35,137
            ret = 4
        str2 = ""
        if offLen[1] == 2:  # length
            str2 = "0"
        else:
            j = int(log2(offLen[1] - 2))
            if j == 0:
                str2 = "1" * (j + 1) + "0"
            else:
                formatInfo = "{0:0" + str(j) + "b}"
                str2 = "1" * (j + 1) + "0" + formatInfo.format(offLen[1] - 2 - 2 ** j)
        destination.write(str1)
        destination.write(str2)
    else:
        destination.write("0" + "{0:08b}".format(ord(char)))
        ret = 0
    return ret


def readable(destination, offLen, char):
    if offLen[1] > 0:
        str1 = " (off: " + str(offLen[0]) + ", len: " + str(offLen[1]) + ") "
        destination.write(str1)
    else:
        destination.write(char)


def regular4_12Bin(destination, offLen, char):
    if offLen[1] > 0:
        str1 = "1" + "{0:012b}".format(offLen[0]) + "{0:04b}".format(offLen[1])
        destination.write(str1)
    else:
        destination.write("0" + "{0:08b}".format(ord(char)))
