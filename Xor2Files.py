def xor(src1, src2):
    f1 = open(src1, "r")
    f2 = open(src2, "r")
    str1 = f1.read()
    str2 = f2.read()
    count = 0
    i = 0
    while i < len(str1) - 1 and i < len(str2) - 1:
        if str1[i] == str2[i]:
            count += 1
        i += 1
    percentage = count / min(len(str1), len(str2))
    return percentage, i, count


def xorArray(src1, src2):
    f1 = open(src1, "r")
    f2 = open(src2, "r")
    f3 = open("files/out/xorTable.txt", "w")
    str1 = f1.read()
    str2 = f2.read()
    count = 0
    i = 0
    while i < len(str1) - 1 and i < len(str2) - 1:
        if str1[i] == str2[i]:
            count += 1
        i += 1
        if 0< i <100:
            tmpString=i.__str__()+ " "+(count/i).__str__()+"\n"
            f3.write(tmpString)
        if 100<i<100000 and i %100 ==0:
            tmpString=i.__str__()+ " "+(count/i).__str__()+"\n"
            f3.write(tmpString)
        if 100000<i<100000000 and i %100000 ==0:
            tmpString=i.__str__()+ " "+(count/i).__str__()+"\n"
            f3.write(tmpString)
    percentage = count / min(len(str1), len(str2))
    return percentage
