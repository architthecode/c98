def swapFileData():
    fileName1 = input("Enter the file name of the first file to swap: ")
    fileName2 = input("Enter the file name of the second file to swap: ")

    with open(fileName1, 'r') as a:
        data_a = a.read()

    with open(fileName2, 'r') as b:
        data_b = b.read()

    with open(fileName1, 'w') as a:
        a.write(data_b)

    with open(fileName2, 'w') as b:
        b.write(data_a)

    with open(fileName1, 'r') as swappedData1:
        readData1 = swappedData1.read()

    with open(fileName2, 'r') as swappedData2:
        readData2 = swappedData2.read()

    print("Files swapped!")
    print("Data in " + fileName1 + ": " + readData1)
    print("Data in " + fileName2 + ": " + readData2)

swapFileData()