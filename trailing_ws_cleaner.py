import sys


def main():
    if len(sys.argv) != 2:
        print("Usage\n   python aboba.py [file name]")
        return
    fileName = sys.argv[1]
    backUpFileName = fileName + ".backup"
    with open(backUpFileName, "w", encoding="utf-8") as backUpFile:
        with open(fileName, encoding="utf-8") as inFile:
            for line in inFile:
                backUpFile.writelines([line])

    with open(backUpFileName, encoding="utf-8") as backUpFile:
        with open(fileName, "w", encoding="utf-8") as outFile:
            for line in backUpFile:
                outFile.write(line.rstrip() + "\n")


if __name__ == '__main__':
    main()
