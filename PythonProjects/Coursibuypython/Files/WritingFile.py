writeFile = 'Example text'
saveFile = open('exampleWrite.txt', 'w')
saveFile.write(writeFile)
saveFile.close()


# appending a file
appendMe = 'Somew Text'

saveFile = open('exampleWrite.txt', 'a')
saveFile.write('\n ')
saveFile.write(appendMe)
saveFile.close()

# code = 'Welcome to coding'
# saveCode = open('Codting.txt','w')
# saveCode.write(code)
# saveCode.close()

# appendCode = 'classes are at'
# saveCode = open('codting.txt', 'a')
# saveCode.write(appendCode)
# saveCode.close()