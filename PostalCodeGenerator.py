def generator(postalCodeStart, postalCodeEnd):
    code_generator = []

    start = postalCodeStart[0:2]
    start += postalCodeStart[3:7]
    start = int(start)
    start += 1

    end = postalCodeEnd[0:2]
    end += postalCodeEnd[3:7]
    end = int(end)

    for i in range(start, end, 1):
        i = str(i)
        new = i[0:2] + "-" + i[2:5]
        code_generator.append(new)

    return code_generator
