import argparse


class Parameters:
    """
    Global parameters

    Another thing that could help us to have a more readable code is
    to declare a class that acts as a global object for the parameters.
    For example, if we want to pass several parameters at the same time
    to a function, we could use this global object, which is the one that 
    contains the global execution parameters.
    """

    def __init__(self, **kwargs):
        self.param1 = kwargs.get("param1")
        self.param2 = kwargs.get("param2")


def view_parameters(input_parameters):
    print(input_parameters.param1)
    print(input_parameters.param2)


parser = argparse.ArgumentParser(description='Testing parameters')
parser.add_argument("-p1", dest="param1", help="parameter1")
parser.add_argument("-p2", dest="param2", help="parameter2")

params = parser.parse_args()

input_parameters = Parameters(param1=params.param1, param2=params.param2)

view_parameters(input_parameters)

"""
$ python3 params_global_argparse.py -p1 hi -p2 hello
hi
hello
"""
