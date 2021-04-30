"""
Let’s see how we can implement our own Context Manager.
This should allow us to understand exactly what’s going
on behind the scenes.
"""

# At the very least a context manager has an __enter__ and __exit__ method defined.

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
