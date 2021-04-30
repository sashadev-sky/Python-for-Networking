def main():
    try:
        with open('test.txt', 'w') as file:
            file.write('this is a test file')
    except IOError as e:
        print('Exception caught: Unable to write to file ', e)
    except Exception as e:
        print('Another error occurred ', e)
    else:
        print('File written to successfully')


if __name__ == '__main__':
    main()


"""
The 'with' statement automatically closes the file even
if an exception is raised.

The code here is equivalent to:
file = open('test.txt', 'w')
try:
    file.write('this is a test file')
finally:
    file.close()
"""
