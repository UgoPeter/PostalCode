string_1 = input("Please enter the beginning of your list of postal codes: ")
string_2 = input("Please enter the end of a list of postal codes: ")

def generator(arg1, arg2):

    code_generator = []
    start = None
    start = arg1[0:2]
    start += arg1[3:7]
    start = int(start)
    start += 1
    end = None
    end = arg2[0:2]
    end += arg2[3:7]
    end = int(end)

    for i in range(start, end, 1):
        i = str(i)
        new = i[0:2] + "-" + i[2:5]
        code_generator.append(new)
        print(code_generator)

generator(string_1, string_2)
    