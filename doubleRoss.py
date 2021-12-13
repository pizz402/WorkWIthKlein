import random

import Encoding


def main(source, randomness):
	f = open(source, "r")  # edit path to file
	src = f.read()
	f.close()
	table1 = {}
	table2 = {}
	# randomness = True  # if True will choose a random table, instead of the maximal one
	# random.seed(10)
	lengths = {}

	# will start at index start and finish and will step forward as long as the chars at these indices are identical
	def rollForward(start, finish):
		length = 0
		while True:
			if finish + length == len(src):  # if true it means the index is outside the document
				return length
			# if length == 16:  # so that when we print the binary code the length int would be under 8 bit
			#	return length
			if src[start + length] == src[finish + length]:  # check identical chars at these locations
				length = length + 1
			else:
				return length  # chars are dissimilar

	def updateTable(index, length):
		if len(src) - index <= 3:
			return
		for x in range(1, length):
			key = src[index - x] + src[index - x + 1] + src[index - x + 2]
			table2.update({key: table1.get(key)})
			table1.update({key: index - x})

	# given a start index i will run backwards attempting to find the offset with the maximal length
	def find(index):  # current index we're at
		off1 = 0
		len1 = 0
		off2 = 0
		len2 = 0
		if len(src) - index > 3:  # not 1 last digits
			key = src[index] + src[index + 1] + src[index + 2]
			if table1.get(key) is not None:
				len1 = rollForward(table1.get(key), index)
				off1 = index - table1[key]
			# if off1 > 4095:
			#	len1 = 0
			if table2.get(key) is not None:
				len2 = rollForward(table2.get(key), index)
				off2 = index - table2[key]
			# if off2 > 4095:
			#	len2 = 0
			if randomness and len1 != 0 and len2 != 0:
				if random.random() > 0.5:
					len1 = len2
					off1 = off2
			if not randomness and len2 > len1:
				len1 = len2
				off1 = off2
			table2.update({key: table1.get(key)})
			table1.update({key: index})
			if len1 < 3:
				len1 = 0
		return off1, len1

	if randomness:
		binary = open("files/out/doubleRoss/outBinRand.txt", "w")
		classic = open("files/out/doubleRoss/outClaRand.txt", "w")
	else:
		binary = open("files/out/doubleRoss/outBin.txt", "w")
		classic = open("files/out/doubleRoss/outCla.txt", "w")

	index = 0
	while index < len(src):
		findResult = find(index)
		Encoding.fromPaperBin(binary, findResult, src[index])
		Encoding.Classic(classic, findResult, src[index])
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
		lengthsFile = open("files/out/doubleRoss/lengthsRand.txt", "w")
	else:
		lengthsFile = open("files/out/doubleRoss/lengths.txt", "w")
	lengthsFile.write(lengths.__str__())
	lengthsFile.close()
