file = open('abc.txt')
# read all content of file
# read n number of character by passing parameter
# print(file.read())
# print(file.readline())
# print(file.readline())
# print line by line using readline
# line = file.readline()
""" while line!= "":
    print(line)
    line = file.readline() """

for line in file.readlines():
    print(line)
# print all text line by line using readlines
file.close()


