try:
    countlines = countchars = 0
    file = open('newfile.txt', 'r')
    lines = file.readlines()
    for line in lines:
        countlines += 1
        for char in line:
            countchars += 1
    file.close()
    print("Characters in file:", countchars)
    print("Lines in file:", countlines)
except IOError as error:
    print("I/O error occurred:", str(error))

"""
$ p3 count_lines_chars.py
Characters in file: 81
Lines in file: 10


If the file we are reading is not available in the same directory,
then it will throw an I/O exception with the following error message:

I/O error occurred: [Errno 2] No such file or directory: ‘newfile.txt’


With writing on the other hand, it creates the file if it doesn't exist
"""
