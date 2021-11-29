def swapFileData(fileName1, fileName2):
    """
    Swap the contents of two files
    """
    with open(fileName1, 'r') as file1:
        with open(fileName2, 'r') as file2:
            file1Data = file1.read()
            file2Data = file2.read()
    with open(fileName1, 'w') as file1:
        with open(fileName2, 'w') as file2:
            file1.write(file2Data)
            file2.write(file1Data)

inputFile1 = input("Enter the name of the first file: ")
inputFile2 = input("Enter the name of the second file: ")
swapFileData(inputFile1, inputFile2)
print("The files have been swapped. have fun")
