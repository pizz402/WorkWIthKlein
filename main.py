import decodeBin
import decodeCla
import Xor2Files
import checkLengths
import doubleMixed
import doublePenta
import doubleQuad
import singlePenta
import singleQuad
import largeLengthFinder
import rossWilliams
import doubleHash
import doubleRoss
import singleHash

# source = "files/sources/text.txt"  # --------------------- change source here --------------------------------
# largeLengthFinder.main(source, randomness)
# print("in Ross")


# source = "D:/Large Texts/dna.100MB.txt"
#print("{0:08b}".format(ord("'")))
#print("{0:08b}".format(ord("h")))
#print("{0:08b}".format(ord("’")))
#print("{0:08b}".format(ord("”")))
source = "D:/Large Texts/text.txt"
#source = "D:/Large Texts/english.200MB.txt"
#source = "D:/Large Texts/code.txt"
#source = "D:/Large Texts/sources.50MB.txt"
destination = "files/out/doubleMixedText/"

#f = open(source, "r")
#txt = f.read()
#f.close()
#newTxt = ""
#for x in range(50000000):
#    if int("{0:08b}".format(ord(txt[x]))) <= 1111111:
#        print(x)
#        newTxt += txt[x]
#new = open("D:/Large Texts/text.txt", "w")
#new.write(newTxt)
#new.close()
##
##
#exit(0)
huffsPaper = ["0", "10", "110", "1110", "1111"]
huffsDNA = [None, None, None, ["0000", "1", "01", "001", "0001"], ["1000", "101", "0", "11", "1001"],
            ["0000", "0001", "01", "1", "001"], ["1000", "1001", "101", "11", "0"]]
huffsText = [None, None, None, ["001", "000", "01", "11", "10"], ["1011", "1010", "100", "11", "0"],
             ["001", "0000", "0001", "01", "1"], ["001", "0000", "0001", "01", "1"]]
# decodeBin.decode("files/out/doubleMixedNew/3Bin0.txt", "files/out/decoded/30.txt", huffs[3])
# decodeBin.decode("files/out/doubleMixedNew/3Bin1.txt", "files/out/decoded/31.txt", huffs[3])
#
#     decodeBin.decode("files/out/doubleMixedNew/"+str(x)+"binRand.txt", "files/out/decoded/3R"+str(flag)+".txt", huffs[3])
# Xor2Files.xorArray("files/out/decoded/30.txt","files/out/decoded/31.txt")
# print(Xor2Files.xor(source, "files/out/decoded/30.txt"))
# print(Xor2Files.xor(source, "files/out/decoded/31.txt"))
fromPaperEncoding = True
randomness = False
for x in range(3, 4):
    #flag = 1
    doubleMixed.main(source, randomness, x, fromPaperEncoding, huffsText[x], destination)
randomness = True
for x in range(3, 4):
    #flag = 1
    doubleMixed.main(source, randomness, x, fromPaperEncoding, huffsText[x], destination)

for x in range(3, 4):
    decodeBin.decode("files/out/doubleMixedText/"+str(x)+"Bin.txt", "files/out/decodedText/"+str(x)+"new.txt", huffsPaper)
    decodeBin.decode("files/out/doubleMixedText/"+str(x)+"BinRand.txt", "files/out/decodedText/"+str(x)+"Rnew.txt", huffsPaper)
    #doubleMixed.mainFlagged(source, randomness, x, fromPaperEncoding, huffsText[x], "files/out/doubleMixedNew/", flag)
    #randomness = True
    #doubleMixed.main(source, randomness, x, fromPaperEncoding, huffsText[x], destination)
    #decodeBin.decode("files/out/doubleMixedText/"+str(x)+"Bin.txt", "files/out/decodedText/"+str(x)+".txt", huffsText[x])
    #decodeBin.decode("files/out/doubleMixedText/"+str(x)+"BinRand.txt", "files/out/decodedText/"+str(x)+"Rand.txt", huffsText[x])
    #decodeBin.decode("files/out/doubleMixedText/"+str(x)+"Bin1.txt", "files/out/decodedText/"+str(x)+"1.txt", huffsText[x])
    #randomness = True
    #doubleMixed.mainFlagged(source, randomness, x, fromPaperEncoding, huffs[x], "files/out/doubleMixedNew/", flag)
    #randomness = True
    #    doubleMixed.mainFlagged(source, randomness, x, fromPaperEncoding, huffs[x], "files/out/doubleMixedNew/", flag)
    #randomness = False
    #doubleMixed.main(source, randomness, x, fromPaperEncoding, huffsText[x], destination)
    #flag = 0
    #doubleMixed.mainFlagged(source, randomness, x, fromPaperEncoding, huffsText[x], destination, flag)
    #flag = 1
    #doubleMixed.mainFlagged(source, randomness, x, fromPaperEncoding, huffsText[x], destination, flag)
#    doubleMixed.mainFlagged(source, randomness, x, fromPaperEncoding, huffs[x], "files/out/doubleMixedNew/", flag)
#
# decodeBin.decode("files/out/doubleMixed/3Bin.txt", "files/out/decoded/3.txt", huffs[3])
# print(x)
# checkLengths.work(source)
#    checkLengths.work(source)
# print("DM vs rand " + str(Xor2Files.xor("files/out/doubleMixed/outBinRand" + str(x) + ".txt","files/out/doubleMixed/outBin" + str(x) + ".txt")))
# checkLengths.work(source)
# print("in Ross")
# rossWilliams.main(source, randomness, adaptive)
# print("in Double Ross")
# doubleRoss.main(source, randomness, adaptive)
# print("in Hash")
# singleHash.main(source, randomness, adaptive)
# print("in doubleHash")
# doubleHash.main(source, randomness, adaptive)
# doublePenta.main(source, randomness, adaptive)
# doubleQuad.main(source, randomness, adaptive)
# singleQuad.main(source, randomness, adaptive)
# singlePenta.main(source, randomness, adaptive)

# print("single hash vs rand " + str(
#    Xor2Files.xor("files/out/singleHash/outBinRand.txt", "files/out/singleHash/outBin.txt")))
# print("double Hash vs rand " + str(
#    Xor2Files.xor("files/out/doubleHash/outBinRand.txt", "files/out/doubleHash/outBin.txt")))
# print("Ross Williams vs rand " + str(
#    Xor2Files.xor("files/out/RossWilliams/outBinRand.txt", "files/out/RossWilliams/outBin.txt")))
# print("double Ross vs rand " + str(
#    Xor2Files.xor("files/out/doubleRoss/outBinRand.txt", "files/out/doubleRoss/outBin.txt")))
# print("DQ vs rand " + str(Xor2Files.xor("files/out/doubleQuad/outBinRand.txt", "files/out/doubleQuad/outBin.txt")))
# print("SQ vs rand " + str(Xor2Files.xor("files/out/singleQuad/outBinRand.txt", "files/out/singleQuad/outBin.txt")))
# print("DP vs rand " + str(Xor2Files.xor("files/out/doublePenta/outBinRand.txt", "files/out/doublePenta/outBin.txt")))
# print("SP vs rand " + str(Xor2Files.xor("files/out/singlePenta/outBinRand.txt", "files/out/singlePenta/outBin.txt")))
# Xor2Files.xorArray("files/out/singlePenta/outBinRand.txt", "files/out/singlePenta/outBin.txt")
#
#
# print(Xor2Files.xor(source, "files/out/doubleMixed/DecodedBin3.txt"))
#
# randomness = True
# fromPaperEncoding = False
# x: int
# for x in range(3, 5):
#    flag = 1
#    doubleMixed.main(source, randomness, x, fromPaperEncoding, huffs[x], flag, "files/out/doubleMixed/")
#    flag = 0
#    doubleMixed.main(source, randomness, x, fromPaperEncoding, huffs[x], flag, "files/out/doubleMixed/")
#
# decodeBin.decode("files/out/doubleMixed/3BinRand.txt", "files/out/doubleMixed/3BinRandDecoded.txt")
# decodeBin.decode("files/out/doubleMixed/4BinRand.txt", "files/out/doubleMixed/4BinRandDecoded.txt")
# decodeBin.decode("files/out/doubleMixed/3BinRandF.txt", "files/out/doubleMixed/3BinRandDecodedF.txt")
# decodeBin.decode("files/out/doubleMixed/4BinRandF.txt", "files/out/doubleMixed/4BinRandDecodedF.txt")
#
# print("decoded 3 rand vs decoded 4 rand")
# print(Xor2Files.xor("files/out/doubleMixed/3BinRandDecoded.txt", "files/out/doubleMixed/4BinRandDecoded.txt"))
#
# print("decoded 3 Flagged vs decoded 3 unFlagged")
# print(Xor2Files.xor("files/out/doubleMixed/3BinRandDecoded.txt", "files/out/doubleMixed/3BinRandDecodedF.txt"))
#
# print("decoded 4 Flagged vs decoded 4 unFlagged")
# print(Xor2Files.xor("files/out/doubleMixed/4BinRandDecoded.txt", "files/out/doubleMixed/4BinRandDecodedF.txt"))
