try:
    myfile = open('newfile.txt', 'wt')
    for i in range(10):
        myfile.write("line #" + str(i+1) + "\n")
    myfile.close()
except IOError as error:
    print("I/O error occurred: ", str(error.errno))


"""
Writing text files is possible using the 'write()' method and it
expects just one argument that represents a string that will
be transferred to an open file.

The open mode 'wt' means that the file is created
in write mode and text format.

writing will create a new file if it doesnt exist
or overwrite the old one
"""
