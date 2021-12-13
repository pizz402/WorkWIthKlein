# check last occurrence of any 2char sequence within max length
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

	# random.seed(10)

	# will start at index start and finish and will step forward as long as the chars at these indices are identical
	def rollForward(start, finish):
		length = 0
		while True:
			if finish + length == len(src):  # if true it means the index is outside of the document
				return length
			if length == 16:  # so that when we print the binary code the length int would be under 8 bit
				return length
			if src[start + length] == src[finish + length]:  # check identical chars at these locations
				length = length + 1
			else:
				return length  # chars are dissimilar

	def updateTable(index, length):
		if len(src) - index <= 2:  # last 2 chars of source, mustn't use them as start of keys, index +2 doesn't exist
			return
		for x in range(1, length):
			key = src[index - x] + src[index - x + 1]
			table.update({key: index - x})

	# given a start index i will run backwards attempting to find the offset with the maximal length
	def find(index):  # current index we're at
		finalOff = 0
		finalLength = 0
		if len(src) - index > 2:  # not 2 last digits
			key = src[index] + src[index + 1]
			if table.__contains__(key):
				finalLength = rollForward(table[key], index)
				finalOff = index - table[key]
				if finalOff > 4095:
					finalLength = 0
			table.update({key: index})
			if finalLength > 4 and randomness:
				if random.random() > 0.5:
					finalLength -= 1

		if finalLength < 3:
			finalLength = 0
		return finalOff, finalLength

	if randomness:
		binary = open("files/out/singleHash/outBinRand.txt", "w")
		classic = open("files/out/singleHash/outClaRand.txt", "w")
	else:
		binary = open("files/out/singleHash/outBin.txt", "w")
		classic = open("files/out/singleHash/outCla.txt", "w")
	# of off|len
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
		lengthsFile = open("files/out/singleHash/lengthsRand.txt", "w")
	else:
		lengthsFile = open("files/out/singleHash/lengths.txt", "w")
	lengthsFile.write(lengths.__str__())
	lengthsFile.close()

# print(table)
