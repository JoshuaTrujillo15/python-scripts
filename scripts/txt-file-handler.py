# Write to .txt file

def overwrite(txtFile, data):
    with open(txtFile, "w") as file:
        file.write(data)

def append(txtFile, data):
    with open(txtFile, "a") as file:
        file.write(data)

def readFile(txtFile, data):
    with open(txtFile, "r") as file:
        file.read()

def readLines(txtFile, data):
    with open(txtFile, "r") as file:
        for line in file:
            print(line)
        

def main():

    txtFile = "" # add file name here, include .txt extension
    data = "test" # replace with content to write to file

    # overwrite(txtFile, data)
    # append(txtFile, data)
    # readFile(txtFile, data)
    # readLines(txtFile, data)


if __name__ == "__main__":
    main()