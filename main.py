import Xor2Files
import checkLengths
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

#print("single hash vs rand " + str(Xor2Files.xor("files/out/singleHash/outBinRand.txt", "files/out/singleHash/outBin.txt")))
#print("double Hash vs rand " + str(Xor2Files.xor("files/out/doubleHash/outBinRand.txt", "files/out/doubleHash/outBin.txt")))
#print("Ross Williams vs rand " + str(Xor2Files.xor("files/out/RossWilliams/outBinRand.txt", "files/out/RossWilliams/outBin.txt")))
#print("double Ross vs rand " + str(Xor2Files.xor("files/out/doubleRoss/outBinRand.txt", "files/out/doubleRoss/outBin.txt")))
#print("DQ vs rand " + str(Xor2Files.xor("files/out/doubleQuad/outBinRand.txt", "files/out/doubleQuad/outBin.txt")))
#print("SQ vs rand " + str(Xor2Files.xor("files/out/singleQuad/outBinRand.txt", "files/out/singleQuad/outBin.txt")))
#print("DP vs rand " + str(Xor2Files.xor("files/out/doublePenta/outBinRand.txt", "files/out/doublePenta/outBin.txt")))
#print("SP vs rand " + str(Xor2Files.xor("files/out/singlePenta/outBinRand.txt", "files/out/singlePenta/outBin.txt")))
# print("in Ross")

source = "D:/Large Texts/english.200MB.txt"
# randomness = False
# rossWilliams.main(source, randomness)
# print("in Double Ross")
# doubleRoss.main(source, randomness)
# print("in Hash")
# singleHash.main(source, randomness)
# print("in doubleHash")
# doubleHash.main(source, randomness)
# doublePenta.main(source, randomness)
# doubleQuad.main(source, randomness)
# singleQuad.main(source, randomness)
# singlePenta.main(source, randomness)
# randomness = False
# print("in Ross")
# rossWilliams.main(source, randomness)
# print("in Double Ross")
# doubleRoss.main(source, randomness)
# print("in Hash")
# singleHash.main(source, randomness)
# print("in doubleHash")
# doubleHash.main(source, randomness)
# doublePenta.main(source, randomness)
# doubleQuad.main(source, randomness)
# singleQuad.main(source, randomness)
# singlePenta.main(source, randomness)
checkLengths.work()