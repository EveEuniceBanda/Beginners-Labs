#INSTRUCTOR NOTE: Run this lab first with lines 10 through 12 commented out
#Opens the file for writing destroys an existing contents
#myFile = open ('file_005.txt', 'w')
myFile = open('file_005.txt', 'w')
myFile.write('abc123')#Writes a single line to the file, without the newline
myFile.write('def456\n')#Writes more text to the file with a newline
myFile.write('ghi789\n')#Writes additional text to the file with a newline
myFile.close()#It is important to ALWAYS close the file!

#First run this program with Lines 10 through 13 commented out
#myFile = open('file_005.txt', 'w')#This opens the file and destroys the contents
#myFile = open('file_005.txt', a+')#This opens the file. Subsequent write commands append to the file
#myFile.write('xyz123\n')
#myFile.close()#close the file again

















