with open("text.txt", "r") as readText:
    readData = readText.read()
    readData = readData.replace('oo', 'ooo')
with open("text.txt", "w") as writeText:
    writeText.write(readData)

