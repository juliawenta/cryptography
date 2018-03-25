#input output module, ability of reading and saving to file in other files


def readFile(fileName):
	file = open(fileName,'r')
	res = file.read()
	file.close()
	return res


def saveFile(fileName,fileBody):
    file = open(fileName, 'w')
    file.write(fileBody)
    file.close()