import RossWilliams
import doubleHash
import doubleRoss
import singleHash


def print_hi(name):
	# Use a breakpoint in the code line below to debug your script.
	print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	print_hi('PyCharm')

# OriginalEncoding8_8.main("C:/Users/user/Desktop/Computer Degree/WorkWithKlein/files/source/text.txt")
# EfficientRecompression.main("C:/Users/user/Desktop/Computer Degree/WorkWithKlein/files/source/text.txt")
RossWilliams4_12.main("C:/Users/user/Desktop/Computer Degree/WorkWithKlein/files/source/text.txt", False)
doubleHash.main("C:/Users/user/Desktop/Computer Degree/WorkWithKlein/files/source/text.txt", False)
singleHash.main("C:/Users/user/Desktop/Computer Degree/WorkWithKlein/files/source/text.txt", False)
doubleRoss.main("C:/Users/user/Desktop/Computer Degree/WorkWithKlein/files/source/text.txt", False)

info = "{0:08b}"
bob = info * 2
print(2 ** 3)

print("in Ross")
# RossWilliams4_12.main("C:/Users/user/Desktop/Computer Degree/much texts/einstein.en.txt")

print("in Original")
# OriginalEncoding8_8.main("C:/Users/user/Desktop/Computer Degree/much texts/einstein.en.txt") #### !!!don't use!!!
# will run twice don't have time to fix

print("in 3rd")
# EfficientRecompression.main("C:/Users/user/Desktop/Computer Degree/much texts/einstein.en.txt")

print("in doubleHash")
# doubleHash.main("C:/Users/user/Desktop/Computer Degree/much texts/einstein.en.txt")

# src = open ("C:/Users/user/Desktop/Computer Degree/much texts/einstein.en.txt", "r")
# print("size of file")
# print(8 * len(src.read()))
# rossReg = open("files/out/RossWilliams/outBin.txt", "r")
# rossRand = open ("files/out/RossWilliams/outBinRand.txt", "r")
# doubleReg = open("files/out/doubleHash/outBin.txt", "r")
# doubleRand= open("files/out/doubleHash/outBinRand.txt", "r")
# print("size of ross")
# print(len(rossReg.read()))
# print("size of ross rand")
# print(len(rossRand.read()))
# print("size of double")
# print(len(doubleReg.read()))
# print("size of double rand")
# print(len(doubleRand.read()))
