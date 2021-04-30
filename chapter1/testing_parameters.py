import argparse

parser = argparse.ArgumentParser(description='Testing parameters')
parser.add_argument("-p1", dest="param1", help="parameter1")
parser.add_argument("-p2", dest="param2", help="parameter2")

params = parser.parse_args()

print(params.param1)
print(params.param2)

"""
$ python3 testing_parameters.py -p1 hi -p2 hello
hi
hello
"""

# otherwise using sys we would want to do something like this

# if __name__ == '__main__':
#     from sys import argv

    # len() - function is used to count the number of arguments passed to the command line.
    # Since the iteration starts with 0, it also counts the name of the program as one argument.
    # If one just wants to deal with other inputs they can use (len(sys.argv)-1).

    # if len(argv) == 3:
    #     print(argv[0])
    #     print(argv[1])
    # else:
    #     print()

"""
$ python3 testing_parameters.py hi hello
testing_parameters.py
hi
"""
