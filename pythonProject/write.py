# read the file and store all the lines in list
# reverse the list
# write the list back to the file
# there is another way to open file in python by using that we dont have to use file.close()

with open('abc.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('abc.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
