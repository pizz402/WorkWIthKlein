def xor(destination1, destination2):
    f1 = open(destination1, "r")
    f2 = open(destination2, "r")
    str1 = f1.read()
    str2 = f2.read()
    sum = 0
    i = 0
    while i < len(str1) - 1 and i < len(str2) - 1:
        if str1[i] == str2[i]:
            sum += 1
        i += 1
    percentage = sum / min(len(str1), len(str2))
    return percentage
