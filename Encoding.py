from math import log2


# noinspection PyTypeChecker
def fromPaperBin(destination, offLen, char):
	if offLen[1] > 0:
		str1 = ""
		if 1 <= offLen[0] <= 64:
			str1 = "1" + "{0:06b}".format(offLen[0])  # 1B_6(d-1)
		elif 64 < offLen[0] <= 320:
			str1 = "01" + "{0:06b}".format(offLen[0] - 65)  # 01B_8(d-65)
		elif 320 < offLen[0] <= 2368:
			str1 = "11" + "{0:011b}".format(offLen[0] - 321)  # 11B_11(d-321)
		else:
			str1 = "110" + "{0:015b}".format(offLen[0] - 2369)  # 111B_15(d-2369)
		str2 = ""
		if offLen[1] == 2:
			str2 = "0"
		else:
			j = int(log2(offLen[1]))
			formatInfo = "{0:0" + str(j) + "b}"
			str2 = "1" * (j + 1) + "0" + formatInfo.format(offLen[1] - 2 - 2 ** j)
		destination.write(str1)
		destination.write(str2)
	else:
		destination.write(char)


def Classic(destination, offLen, char):
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
